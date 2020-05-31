# -*- coding: utf-8 -*-
import numpy as np
from skimage import io
'''
土地利用模块

土地利用类型：
0---水体
1---森林
2---草地
3---农田
4---建城区
5---未利用
'''

def get_Lucc_present(filename='Lucc.tif',filepath='./data/'):
    '''
    返回初始的土地利用类型
    ---
    Input:
    None
    ---
    Output:
    img (np.array) 初始土地利用
    ''' 
    img = io.imread(filepath+filename)#读取Lucc
    img[img==128] = -1  #缺失值设为-1
    # img[img==0] = 0   #水体设为0
    img[(img >=1) & (img < 6)] = 1  #森林设为1
    img[(img >=6) & (img < 12)] = 2  #草地设为2
    img[img==12] = 3  #农田设为3
    img[img==13] = 4  #建城区设为4
    img[(img > 13) & (img < 17)] = 5  #未利用设为5
    return img


# %%
'''
import gdal
import numpy as np
import os
from skimage import io
class Dataset:
    def __init__(self, in_file):
        self.in_file = in_file

        dataset = gdal.Open(self.in_file)
        self.XSize = dataset.RasterXSize  # 网格的X轴像素数量
        self.YSize = dataset.RasterYSize  # 网格的Y轴像素数量
        self.GeoTransform = dataset.GetGeoTransform()  # 投影转换信息
        self.ProjectionInfo = dataset.GetProjection()  # 投影信息

    def get_lon_lat(self):
        gtf = self.GeoTransform
        x_range = range(0, self.XSize)
        y_range = range(0, self.YSize)
        x, y = np.meshgrid(x_range, y_range)
        lon = gtf[0] + x * gtf[1] + y * gtf[2]
        lat = gtf[3] + x * gtf[4] + y * gtf[5]
        return lon, lat
dir_path = r"D:/综合评估模型  算法与实践/LCP/data"
filename = "Lucc.tif"
file_path = os.path.join(dir_path, filename)
dataset = Dataset(file_path)

value = io.imread(file_path).astype(np.float64)
longitude, latitude = dataset.get_lon_lat()
image_size = longitude.shape
mask = np.zeros((3, image_size[0], image_size[1])).astype(np.float64) 
mask[0]=longitude
mask[1]=latitude
mask[2]=value
file_path = os.path.join(dir_path, "new_Lucc2.tif")
io.imsave(file_path, np.float64(mask))
'''