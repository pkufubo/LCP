# -*- coding: utf-8 -*-
import numpy as np
import csv
from sklearn import linear_model 

import pop_fct
import Lucc_fct
'''
粮食农田模块

五种农作物指粮食、油料、棉花、糖类、蔬菜

'''


def get_area_output(year,filename='output_per_area.csv',filepath='./data/'):
    '''
    得到对五类农作物单位面积产量
    ---
    Input:
    year (int)  年份
    ---
    Output:
    [output0,output1,output2,output3] (list) [单位面积产量0-3]
    '''    
    # 数据来源自国家统计局
    # 单位面积农作物产量 （公斤/公顷）

    TMP= np.array([line for line in csv.reader(open(filepath+filename
        ,'r'))], dtype=np.float32)
    output = []
    for i in range(5):
        model = linear_model.LinearRegression()
        model.fit(TMP[0].reshape(-1,1), TMP[1+i].reshape(-1,1))
        output.append(model.predict([[year]]).reshape(1)[0])
    return np.array(output[:4])

def get_area_propotion():
    '''
    几种农作物播种面积比例
    ---
    Input:
    None
    ---
    Output:
    [propotion0,propotion1,propotion2,propotion3] (list) [播种面积0-3]
    '''    
    # 数据来源自国家统计局
    # 2019年播种面积 （千公顷）    
    TOTAL = 165930.66
    FOOD_CROPS = 116063.6
    OIL_CROPS = 12925.43
    COTTON_CROPS = 3339.29
    SUGAR_CROPS = 1620
    return np.array([x/TOTAL for x in [FOOD_CROPS,OIL_CROPS,COTTON_CROPS,SUGAR_CROPS]])
    
def get_capital_demand():
    '''
    得到对五类农作物人均需求量/占有量的增长率
    ---
    Input:
    None
    ---
    Output:
    [r0,r1,r2,r3] (list) [增长率0-3]
    '''
    return np.array([0,0,0,0])

def crop_year(year):
    '''
    根据农产品需求得到的农田相对于2020年的系数
    ---
    Input:
    year (int)
    ---
    Output:
    r (float) 最少应为2020年的r倍  
    '''
    present_year = 2020
    alpha_pop = pop_fct.get_pop_total_year(year)/pop_fct.get_pop_total_year(present_year)
    alpha_capital_demand = get_capital_demand()+1
    alpha_area_output = get_area_output(present_year)/get_area_output(year)
    
    alpha = alpha_pop*alpha_capital_demand*alpha_area_output
    alpha_total = (alpha*get_area_propotion()).sum()/get_area_propotion().sum()
    ### 耕地红线约束
    RED_LINE = 18e8*0.0006667  # 18亿亩耕地红线
    Lucc_present = Lucc_fct.get_Lucc_present(filename='Lucc.tif',filepath='./data/')
    crop_area = (Lucc_present==3).sum()
    return np.max([alpha_total,RED_LINE/crop_area])
