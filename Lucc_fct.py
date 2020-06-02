# -*- coding: utf-8 -*-
import numpy as np
import gdal
from skimage import io

'''
土地利用模块

土地利用类型编码：
-1 --- 缺失值
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

def get_lon_lat(filename='Lucc.tif',filepath='./data/'):
    '''
    返回经纬度数据
    ---
    Input:
    None
    ---
    Output:
    lon,lat (np.array) 经度和维度
    ''' 
    dataset = gdal.Open(filepath+filename)
    gtf = dataset.GetGeoTransform()
    x_range = range(0, dataset.RasterXSize)
    y_range = range(0, dataset.RasterYSize)
    x, y = np.meshgrid(x_range, y_range)
    lon = gtf[0] + x * gtf[1] + y * gtf[2]
    lat = gtf[3] + x * gtf[4] + y * gtf[5]
    return lon, lat
# %%
