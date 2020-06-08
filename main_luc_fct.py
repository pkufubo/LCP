# -*- coding: utf-8 -*-

'''
主模块：土地利用变化模块
'''

import Lucc_fct
import house_fct
import crop_fct

import numpy as np

def count_luc_class(Lucc,luc_class):
    '''
    返回每个格点周围临近格点，满足某种土地利用类型的数目
    ---
    Input:
    Lucc 当前的土地利用数据
    luc_class 查的土地利用类型
    ---
    Output:
    Lucc_count_class 计数
    '''
    pass
    size = Lucc.shape
    Lucc_count_class = np.zeros(size)
    bool_Lucc = Lucc==luc_class
    ####
    # 上方是否是目标类型
    Lucc_count_class[1:,:] += bool_Lucc[:-1,:]
    # 下方是否是目标类型
    Lucc_count_class[:-1,:] += bool_Lucc[1:,:]
    # 左方是否是目标类型
    Lucc_count_class[:,1:] += bool_Lucc[:,:-1]
    # 右方是否是目标类型
    Lucc_count_class[:,:-1] += bool_Lucc[:,1:]
    #####
    # 左上方是否是目标类型
    Lucc_count_class[1:,1:] += bool_Lucc[:-1,:-1]
    # 右上方是否是目标类型
    Lucc_count_class[1:,:-1] += bool_Lucc[:-1,1:]
    # 左下方是否是目标类型
    Lucc_count_class[:-1,1:] += bool_Lucc[1:,:-1]
    # 右下方是否是目标类型
    Lucc_count_class[:-1,:-1] += bool_Lucc[1:,1:]
    return Lucc_count_class+1


Lucc_present = Lucc_fct.get_Lucc_present(filename='Lucc.tif',filepath='./data/')
crop_land_present = np.sum(Lucc_present==3)

year = 2050

crop_alpha = crop_fct.crop_year(year)
house_alpha = 1.05
forest_alpha = 26/23 #国家林业局
grassland_alpha = 1.05

Lucc_next = Lucc_present.copy()
###  第一步建筑用地
size = Lucc_present.shape
random_list = np.random.rand(size[0],size[1])
weight = count_luc_class(Lucc_present,4)
w_random_list = random_list*weight
w_random_list = (1-(Lucc_present==-1))*(1-(Lucc_present==4))\
    * (1-(Lucc_present==0)) * w_random_list #水体不能盖房子

sort_random = np.sort(w_random_list.reshape(size[0]*size[1]))
n_need = int((house_alpha-1)*(Lucc_present==4).sum())
Lucc_next[w_random_list>=sort_random[-n_need]] = 4 ##被选出的区域变成了建筑用地

###  第二步 草地/林地
size = Lucc_present.shape
random_list = np.random.rand(size[0],size[1])
weight = count_luc_class(Lucc_present,2)
w_random_list = random_list*weight
w_random_list = (1-(Lucc_present==-1))*(1-(Lucc_present==1))*(1-(Lucc_present==2))\
    * (1-(Lucc_present==0))* (1-(Lucc_present==4))* w_random_list #林草不互变

sort_random = np.sort(w_random_list.reshape(size[0]*size[1]))
n_need = int((grassland_alpha-1)*(Lucc_present==2).sum())
Lucc_next[w_random_list>=sort_random[-n_need]] = 2 ##被选出的区域变成了草地


size = Lucc_present.shape
random_list = np.random.rand(size[0],size[1])
weight = count_luc_class(Lucc_present,1)
w_random_list = random_list*weight
w_random_list = (1-(Lucc_present==-1))*(1-(Lucc_present==1))*(1-(Lucc_present==2))\
    * (1-(Lucc_present==0))* (1-(Lucc_present==4))* w_random_list #林草不互变

sort_random = np.sort(w_random_list.reshape(size[0]*size[1]))
n_need = int((forest_alpha-1)*(Lucc_present==1).sum())
Lucc_next[w_random_list>=sort_random[-n_need]] =1 ##被选出的区域变成了森林

###  第三步 农田

# (Lucc_next==3)

# test = count_luc_class(Lucc_present,1)
# plt.imshow(test)
# plt.colorbar()
# plt.title('Weight from neighbors for forest')


