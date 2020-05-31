# -*- coding: utf-8 -*-
import numpy as np
import csv
'''
人口模块
'''

def get_pop(filename='SSPs_POP_ssp2.csv',filepath='./data/'):
    '''
    读入人口数据
    ---
    Input:
    filenam (str)  人口数据的csv文件
    filepath (str) 人口数据所在的路径
    ---
    Output:
    [lon,lat,pop] (list) (经度，维度，人口2010-2100)
    '''
    TMP= np.array([line for line in csv.reader(open(filepath+filename
        ,'r'))], dtype=np.float32)
    lon = TMP[:,0]
    lat = TMP[:,1]
    pop = TMP[:,2:]
    
    return [lon,lat,pop]

# %%
