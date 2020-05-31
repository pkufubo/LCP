import matplotlib.pylab as plt
from matplotlib.colors import ListedColormap

def get_luc_cmap():
    '''
    土地利用变化画图使用的cmap
    Returns
    cmap
    -------
    None.

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