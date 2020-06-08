import numpy as np
from skimage import io
from skimage.transform import resize
import scipy.ndimage as ndimage

def main():
    pop2010 = io.imread('2010.tif')
    pop2050 = io.imread('2050.tif')
    Lucc = io.imread('new_lucc.tif')
    lucc_new = resize(Lucc, pop2010.shape, order=0, mode='edge', cval=0, clip=True, preserve_range=True)
    lucc_new = np.where(lucc_new == 128, -128, lucc_new)
    io.imsave('new_lucc_3.tif',np.float32(lucc_new))
    #cal_pop_density(lucc_new, pop)
    cal_pop_density_for_pixel(lucc_new, pop2010, pop2050)



def cal_pop_density(lucc, pop):
    class_map = (lucc == 13).astype(int)
    pop = pop*class_map
    a = pop[pop > 0]
    # pixel = (0.5/0.0083)*2
    #
    # pop = np.where(pop > 0, pop/pixel, 0)
    # io.imsave('density.tif', np.float32(pop))

    print('pop_2010: ', sum(a))
    ratio = sum(a)/1300000000
    area_2010 = len(a)*(0.5/0.0083)*2
    print('area_2010: ', area_2010)

    pop_2050 = 1404374503
    city_pop_2050 = pop_2050 * ratio
    density = np.sum(a) / area_2010
    print('density_2010: ', density)
    area_2050_1 = city_pop_2050 / density
    area_2050_2 = city_pop_2050 / (density*1.05)
    area_2050_3 = city_pop_2050 / (density*1.10)
    print('area for 1.0 * density_2010: ', area_2050_1)
    print('area for 1.05 * density_2010: ', area_2050_2)
    print('area for 1.10 * density_2010: ', area_2050_3)

def cal_pop_density_for_pixel(lucc, pop2010, pop2050=None):
    class_map = (lucc == 13).astype(int)
    pop2010 = pop2010 * class_map
    pixel = (0.5 / 0.0083) * 2

    density2010_105 = np.where(pop2010 > 0, 1.05 * pop2010 / pixel, 0)
    density2010_110 = np.where(pop2010 > 0, 1.10 * pop2010 / pixel, 0)

    pop2050 = pop2050 * class_map
    area2050_105 = pop2050 / density2010_105
    area2050_110 = pop2050 / density2010_110
    area2050_105 = np.where(area2050_105 < 10000, area2050_105, 0)
    area2050_110 = np.where(area2050_110 < 10000, area2050_110, 0)

    area_sum_105 = sum(area2050_105[area2050_105 > 0])
    print(area_sum_105)
    area_sum_110 = sum(area2050_110[area2050_110 > 0])
    print(area_sum_105, area_sum_110)
    io.imsave('density_105.tif', np.float32(area2050_105))
    io.imsave('density_110.tif', np.float32(area2050_110))

if __name__ == '__main__':
    main()