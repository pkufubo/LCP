import matplotlib.pylab as plt
from matplotlib.colors import ListedColormap
import matplotlib.ticker as ticker
import numpy as np
'''
画图模块
'''

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

def plot_POP(lon,lat,pop,title='POP'):
    '''
    绘制人口的空间分布
    ---
    Input:
    lon  经度
    lat  维度
    pop  人口
    ---
    Output:
    None
    '''    
    s1 = plt.scatter(lon,lat,c=np.log10(pop),
                cmap="RdBu_r")
    def fmt(x,pos):
        return r'$10^{}$'.format(int(x))
    plt.colorbar(s1,shrink=1, aspect=5,format=ticker.FuncFormatter(fmt))#    
    plt.title(title)