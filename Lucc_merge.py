import numpy as np
from skimage import io
import matplotlib.pylab as plt

import plot_fct

img = io.imread('Lucc.tif')#读取Lucc

img[img==128] = -1  #缺失值设为-1
# img[img==0] = 0   #水体设为0
img[(img >=1) & (img < 6)] = 1  #森林设为1
img[(img >=6) & (img < 12)] = 2  #草地设为2
img[img==12] = 3  #农田设为3
img[img==13] = 4  #建成区设为4
img[(img > 13) & (img < 17)] = 5  #未利用设为5
plt.imshow(img,cmap=plot_fct.get_luc_cmap())
plt.colorbar()

io.imsave('new_lucc.tif',np.float16(img))#写出tiff
