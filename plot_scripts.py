import matplotlib.pylab as plt
from matplotlib.colors import ListedColormap
import matplotlib.ticker as ticker
import numpy as np
from skimage import io
import csv

import Lucc_fct
import pop_fct
'''
画图脚本
'''
# %%
# 一些画图辅助函数
from matplotlib.colors import ListedColormap
def get_luc_cmap():
    '''
    土地利用变化画图使用的cmap
    ---
    Input:
    None
    ---
    Output:
    ListedColormap
    '''
    # LUC_type = ['缺失',
    #             '水体','森林','草地',
    #             '农田','建城区',
    #             '未利用']
    color_list = ['lightgrey',
                  'cyan','darkgreen','limegreen',
                  'orange','purple',
                  'olive'] 
    return ListedColormap(color_list)

#%%
# 绘制初始土地利用图
Lucc_present = Lucc_fct.get_Lucc_present()
# plt.imshow(Lucc_present,cmap=get_luc_cmap())
plt.imshow(Lucc_next,cmap=get_luc_cmap())
def fmt(x,pos):
    if x<0:
        return r'N/A'
    elif x<1:
        return r'Water'
    elif x<2:
        return r'Forest'
    elif x<2.5:
        return r'Grossland'
    elif x<3.9:
        return r'Cropland'
    elif x<4:
        return r'Constructionland'
    elif x<6:
        return r'Not used'
    return r'???'
plt.colorbar(shrink=1, aspect=2,ticks=[-0.5,
                                       0.3,  1.2,  2,
                                       2.8,  3.8,
                                       4.5],format=ticker.FuncFormatter(fmt))
plt.title(r'Land use cover')

# %%
# 绘制人口的空间分布
ssp = '1'
filename='SSPs_POP_ssp'+ssp+'.csv'
lon,lat,pop = pop_fct.get_pop()
pop_plot = pop[:,2050-2010]
pop_plot = pop[:,2020-2010]
s1 = plt.scatter(lon,lat,c=np.log10(pop_plot),
            cmap="RdBu_r")
def fmt(x,pos):
    return r'$10^{}$'.format(int(x))
plt.colorbar(s1,shrink=1, aspect=5,format=ticker.FuncFormatter(fmt))#
title = 'SSP'+ssp+' '+'2050'   
title = '2020 population input'
plt.title(title)    
# %%
# 绘制Hi和Wi
filepath = './'
filename = 'Wi.tif'
img = io.imread(filepath+filename)
img[img<=0]=0
img[img>=240]=240
plt.imshow(img)
plt.colorbar()
plt.title('Wi')
# %%
filepath = './'
filename = 'Hi.tif'
img = io.imread(filepath+filename)
img[img<=1.5]=1.5
img[img>=15.5]=15.5
plt.imshow(img)
plt.colorbar()
plt.title('Hi')
# %%
filename='output_per_area.csv'
filepath='./data/'
TMP= np.array([line for line in csv.reader(open(filepath+filename
    ,'r'))], dtype=np.float32)
for i in range(5):
    fig, axs = plt.subplots()
    axs.scatter(TMP[0],TMP[i+1])
    axs.set_title('crop'+str(i))
    fig.savefig('crop'+str(i)+'.png',dpi=150)
# %%
filepath = './data/'
filename = 'Precipitation.tif'
img = io.imread(filepath+filename)
img[img<0]=0
plt.imshow(img)
plt.colorbar()
plt.title('Precipitation')
# %%
filepath = './data/'
filename = 'Temperature.tif'
img = io.imread(filepath+filename)
img[img<0]=0
plt.imshow(img)
plt.colorbar()
plt.title('Temperature')

# %%
filepath = './'
filename = 'forest.tif'
img = io.imread(filepath+filename)
plt.imshow(img)
plt.colorbar()
plt.title('grass')
# %%
filepath = './'
filename = 'new_lucc_2.tif'
img = io.imread(filepath+filename)
img = np.array(img,dtype=int)
plt.imshow(img)
plt.colorbar()