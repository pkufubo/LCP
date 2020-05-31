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

def get_pop_total_year(year):
    '''
    返回某一年总人口数
    ---
    Input:
    year (int)  年份
    ---
    Output:
    pop (int) 总人口数
    '''
    assert year in range(2010,2100+1),'只能以2010-2100的年份为输入变量'
    pop_data = get_pop()
    return pop_data[2][:,year-2010].sum(0)

def get_pop_total_timeseries(start=2010,end=2100):
    '''
    返回总人口数的时间序列
    ---
    Input:
    start (int) 开始年份
    end (int) 截止年份
    ---
    Output:
    pop (int) 总人口数
    '''
    assert start in range(2010,2100+1),'只能以2010-2100的年份为输入变量'
    assert end in range(2010,2100+1),'只能以2010-2100的年份为输入变量'
    pop_data = get_pop()
    return pop_data[2][start-2010:end-2010+1].sum(0)
