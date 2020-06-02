# LCP

Land cover planning model
土地覆盖规划模型

## 项目说明

- 目的：预测2050年中国土地利用的空间格局和变化路径
- 背景：北京大学研究生课程《综合评估模型：算法与实践》期末作业

## 作者信息

徐静  北京大学城市与环境学院19级博士研究生 1901111765  
付博  北京大学城市与环境学院18级博士研究生 1800013223

## 模型架构

pass

## 模块介绍

### 土地利用类型模块

- **模块功能**

  - 读写土地利用类型数据(tiff文件)
  - 对原始土地利用类型重新分类

- **模块说明**
  - 重新编码

    为了简化模型，将原始数据中的17种类型重新编码为本模型中的5种土地利用类型。

    |编码|类型|原编码|原类型|
    |----|----|----|------|
    |**0**|**水体**|0|Water|
    |**1**|**森林**|1|Evergreen Needle-leaf forest|
    |**1**|**森林**|2|Evergreen Broad-leaf forest|
    |**1**|**森林**|3|Deciduous Needle-leaf forest|
    |**1**|**森林**|4|Deciduous Broad-leaf forest|
    |**1**|**森林**|5|Mixed forest|
    |**2**|**草地**|6|Closed shrublands|
    |**2**|**草地**|7|Open shrublands|    
    |**2**|**草地**|8|Woody savannas|
    |**2**|**草地**|9|Savannas|
    |**2**|**草地**|10|Grasslands|
    |**2**|**草地**|11|Permanent wetlands|
    |**3**|**农田**|12|Croplands|
    |**4**|**建城区**|13|Urban and built-up|
    |**5**|**未利用**|14|Cropland/Natural vegetation mosaic|
    |**5**|**未利用**|15|Permanent snow and ice|
    |**5**|**未利用**|16|Barren or sparsely vegetated|
    |**-1**|**未利用**|255|Fill Value|

### 粮食农田模块

- **模块功能**

    预测某一年所需要的耕地面积。

- **基本约束**
  - 现行中国18亿亩耕地红线，全国划定永久基本农田15.5亿亩。
  
- **模块假设**
  - 人均对粮食、油料、棉花、糖类的需求不变
  - 我国种植各类农产品的耕地比例不变
  - 各类农产品的亩产逐年有稳定增长
  - 各类农产品的进口占比不变
