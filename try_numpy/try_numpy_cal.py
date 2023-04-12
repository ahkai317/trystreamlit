# -*- coding: utf-8 -*-
import numpy as np


#======================================================
# 基礎運算

#======================================================
# 逐元運算 - Elementwise
# 針對陣列中的每個資料，逐一進行基本運算

# 建立兩個多維陣列
data = np.array([3, 4, 1])
data2 = np.array([-2, 5, -8])

#------------------------------------------------
# 算數運算子
data + data2    # Output: array([ 1,  9, -7])
data - data2    # Output: array([ 5, -1,  9])
data * data2    # Output: array([-6, 20, -8])
data / data2    # Output: array([-1.5  ,  0.8  , -0.125])

#------------------------------------------------
# 比較運算子
data > data2    # Output: array([ True, False,  True])
data == data2   # Output: array([False, False, False])
data <= data2   # Output: array([False,  True, False])


#======================================================
# 矩陣運算 - Matrix
# 針對兩個陣列進行矩陣運算

data = np.array([   # 2d-array; Shape: (1, 2)
    [1, 3]
])

data2 = np.array([  # 2d-array; Shape: (2, 3)
    [2, -1, 3],
    [-2, 4, 1]
])

print(data, data2)

#------------------------------------------------
# 內積
# 要做內積，兩矩陣 例如： (1, 2) (2, 3) 的 2 需要對上
# Shape: (1, 2) with (2, 3) -> (1, 3)
print('內積：', data.dot(data2)) # Output: array([[-4, 11,  6]])
                                # -> ( -4 = 1*2 + 3*(-2) ), ( 11 = 1*(-1) + 3*4 ), ( 6 = 1*3 + 3*1 )
# print('內積：', data @ data2)

#------------------------------------------------
# 外積
# Shape: (1, 2) with (2, 3) -> (2, 6)
print('外積：', np.outer(data, data2))   # Output: array([[ 2, -1,  3, -2,  4,  1],
                                        #                [ 6, -3,  9, -6, 12,  3]])


#======================================================
# 統計運算 - Statistics
# 又稱單元運算，只需要一個矩陣的資料就可以運算了


data = np.array([
    [2, 1, 7],
    [-5, 3, 8]
])

result = data.sum()
print('總和：', result)     # Output: array([-3,  4, 15])

result = data.max()
print('最大值：', result)   # Output: array([-3,  4, 15])

result = data.mean()
print('平均值：', result)   # Output: array([-3,  4, 15])

result = data.std()
print('標準差：', result)   # Output: array([-3,  4, 15])

#------------------------------------------------
# 軸向統計
result = data.sum(axis = 0)
print('對 第一軸 (column) 做總和：', result)    # Output: array([-3,  4, 15])

result = data.sum(axis = 1)
print('對 第二軸 (row) 做總和：', result)       # Output: array([10,  6])


#------------------------------------------------
# 逐值累加 - Cumulative
result = data.cumsum()
print('逐值累加：', result)     # Output: array([ 2,  3, 10,  5,  8, 16])

result = data.cumsum(axis = 0)
print('對 第一軸 (column)，逐值累加：', result)     # Output: array([[ 2,  1,  7],
                                                #                [-3,  4, 15]])
result = data.cumsum(axis = 1)
print('對 第二軸 (row)，逐值累加：', result)    # Output: array([[ 2,  3, 10],
                                            #                [-5, -2,  6]])

#------------------------------------------------
# 切片統計
