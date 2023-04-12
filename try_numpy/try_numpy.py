# -*- coding: utf-8 -*-
"""
try_numpy.py
    - numpy 常用情境 & 基本介紹
@ Created on 23.04.07
"""

import numpy as np

# Indexing with slices

##########################################################
# 常用 method
array = np.arange(0, 5)
arr2d.ndim
arr2d.shape


#======================================================
# 一維陣列 one-dimensional array
arr3 = np.arange(0, 10)
arr3

slice_24 = arr3[2:5] #切片 [2][3][4], 請注意!是一個view

#變更 arr3 的值
arr3[2:4] = arr3[2:4] * 100

#檢視 arr3
arr3 #array([  0,   1, 200, 300,   4,   5,   6,   7,   8,   9])

#檢視 slice_24
slice_24 #array([200, 300,   4])

#======================================================
# 二維陣列 two-dimensional array

arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr2d

arr2d.ndim
arr2d.shape

np.random.randint(-2, 4, (2, 3)) # 2x3, 2d

#case 1:
#slice of arr2d, 沿著 axis0 (第一軸) 切
arr2d[:2]

#先沿 axis0 切[:2],
#再沿 axis1 切[1:]
s=arr2d[:2,1:]
s  #結果是一個 ndarray shape(2,2), 但還是 view

#更新arr2d 的值
arr2d[:,:]=arr2d[:,:]*100
arr2d
s #但還是 view

#先回到原先的 arr2d 繼續 slicing 介紹
arr2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
arr2d

#------------------------------------------------
#case 2:
#a. 單純 index axis=0
arr2d[2] #array([7, 8, 9])
arr2d[2].shape #(3,)

#b. 第一軸 indexing, 第二軸 slicing
arr2d[2,:] #array([7, 8, 9])
arr2d[2,:].shape #(3,)

#c. 第一軸 slice 2:, 第二軸 slice :
arr2d[2:,:] # array([[7, 8, 9]])
arr2d[2:,:].shape #(1,3)

#-------------------------------------------
#case 3: 第一軸 slice :, 第二軸 slice :2
arr2d[:,:2]
arr2d[:,:2].shape #(3,2)

#--------------------------------------------
#case 4:
#a. 第一軸 index 1, 第二軸 slice :2
arr2d[1,:2] #array([4, 5])
arr2d[1,:2].shape #(2,)

#b. 第一軸 slice 1:2, 第二軸 slice :2
arr2d[1:2,:2] #array([[4, 5]])
arr2d[1:2,:2].shape #(1,2)

#==============================================
#assigning to a slice expression assigns to the whole selection
arr2d[:, :1] = 0
arr2d

#======================================================
#練習: 比較 arr2d[:2,1:] 與 arr2d[:2][1:] 的差異
arr2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
