import numpy as np
from skimage import io
img = io.imread('Lucc.tif')#读取Lucc
# print(img.shape)
# print(img.dtype)
img=np.where((img > 0) & (img < 6), 1, img)
img=np.where((img > 5) & (img < 12), 2, img)
img[img==12]=3
img[img==13]=4
img=np.where((img > 13) & (img < 17), 5, img)

io.imsave('new_lucc.tif',np.float16(img))#写出tiff

