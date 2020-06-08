import numpy as np
from skimage import io
from glob import glob
import matplotlib.pyplot as plt

def select(wi_low, hi_low, name, wi_high=None, hi_high=None):# 选出符合Wi和Hi阈值的土地
    Wi = io.imread('Wi.tif')
    Hi = io.imread('Hi.tif')
    if(wi_high is not None):#设定Wi和Hi的范围
        Wi = ((Wi > wi_low) & (Wi < wi_high))
    else:
        Wi = (Wi > wi_low)
    if (hi_high is not None):
        Hi = ((Hi > hi_low) & (Hi < hi_high))
    else:
        Hi = (Hi > hi_low)
    mask = (Wi & Hi).astype(int)
    io.imsave(name+'.tif', np.float16(mask))

def segmentation(c): #选出class=c的Wi和Hi
    Wi = io.imread('Wi.tif')
    Hi = io.imread('Hi.tif')
    lucc = io.imread('new_lucc.tif')
    class_map = (lucc == c).astype(int)
    Wi = Wi * class_map
    Hi = Hi * class_map
    # io.imsave('Wi_class%d.tif'%c, np.float32(Wi))
    # io.imsave('Hi_class%d.tif'%c, np.float32(Hi))
    wi_high = np.max(Wi)
    hi_high = np.max(Hi)
    Wi_temp = np.where(Wi <= 0, wi_high, Wi)
    Hi_temp = np.where(Hi <= 0, hi_high, Hi)
    wi_low = np.min(Wi_temp)
    hi_low = np.min(Hi_temp)

    Wi_temp = Wi[(Wi >= wi_low) & (Wi <= wi_high)]
    Hi_temp = Hi[(Hi >= hi_low) & (Hi <= hi_high)]

    return Wi_temp, Hi_temp


def main():#计算 Hi and Wi
    data_paths = glob('temperature/*')
    P = io.imread('Precipitation.tif')*12
    Wi = np.zeros(P.shape).astype(np.float32)

    for i in data_paths:
        img = io.imread(i)
        img = np.where((img > 5) | (img < -1000), img-5, 0)
        Wi += img
    Wi = np.where((Wi < -1000), -32768.0, Wi)
    io.imsave('Wi.tif', np.float32(Wi))

    x = (Wi != 0).astype(int)
    Wi = np.where(Wi > 0, Wi, 1)
    Hi = P / Wi
    Hi = Hi * x
    io.imsave('Hi.tif', np.float32(Hi))

# def draw(Hi):
#     plt.figure("pic")
#     n, bins, patches = plt.hist(Hi, bins=256, normed=1, facecolor='green', alpha=0.75)
#     plt.show()

def cal_lower_and_upper(data):#计算耕地Hi的合理覆盖范围：均值左右各取0.475
    avg = np.mean(data)
    max = np.max(data)
    min = np.min(data)
    lower = (avg-(avg-min)*0.475)
    upper = (avg+(max-avg)*0.475)
    print(lower, upper)
    return lower, upper

if __name__=='__main__':
    #main()
    select(45, 7.5, 'forest')
    select(0, 3.5, 'grass', hi_high=7.7)
    Wi, Hi = segmentation(3)
    Hi = Hi[Hi < 20]
    hi_lower, hi_upper = cal_lower_and_upper(Hi)
    select(0, hi_lower, 'croplands', hi_high=hi_upper)
