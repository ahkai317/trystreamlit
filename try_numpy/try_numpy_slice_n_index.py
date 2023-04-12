# -*- coding: utf-8 -*-
import numpy as np

#======================================================
# 索引 & 切片

#------------------------------------------------
# Case 1:

# 沿著 axis0 (第一軸) 切
arr_2d[:2]  # Output: array([[1, 2, 3],
            #                [4, 5, 6]])

# 先沿 axis0 切 [:2]
# 再沿 axis1 切 [1:]
s = arr_2d[:2, 1:]
s  # Output: array([[2, 3],
   #                [5, 6]])
   # 結果是一個 ndarray shape(2, 2), 但還是 view

# 更新 arr_2d 的值
arr_2d[:, :] = arr_2d[:, :] * 100
arr_2d
s # 但還是 view

# 先回到原先的 arr_2d 繼續 slicing 介紹
arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr_2d


#------------------------------------------------
# Case 2:

# 單純 index axis = 0
arr_2d[2]       # Output: array([7, 8, 9])
arr_2d[2].shape # Output: (3,)

# 第一軸 indexing, 第二軸 slicing
arr_2d[2, :]         # Output: array([7, 8, 9])
arr_2d[2, :].shape   # Output: (3,)

# 第一軸 slice 2:, 第二軸 slice :
arr_2d[2:, :]        # Output: array([[7, 8, 9]])
arr_2d[2:, :].shape  # Output: (1, 3)


#-------------------------------------------
# Case 3: 第一軸 slice :, 第二軸 slice :2
arr_2d[:, :2]       # Output: array([[1, 2],
                    #                [4, 5],
                    #                [7, 8]])
arr_2d[:, :2].shape # Output: (3, 2)


#--------------------------------------------
# Case 4:

# 第一軸 index 1, 第二軸 slice :2
arr_2d[1, :2]        # Output: array([4, 5])
arr_2d[1, :2].shape  # Output: (2,)

# 第一軸 slice 1:2, 第二軸 slice :2
arr_2d[1:2, :2]          # Output: array([[4, 5]])
arr_2d[1:2, :2].shape    # Output: (1,2)


#--------------------------------------------
# 全部都要
arr_2d[:]
arr_2d[...]

# 三維陣列的情況
data = array([[[ 3,  1,  2],
               [ 1,  0,  5]],
              [[ 5,  4,  3],
               [ 1,  3, -3]]])

data[..., 0:2]  # 此寫法，第二個 slice 會直切最後一層
                # Output: array([[[3, 1],
                #                 [1, 0]],
                #                [[5, 4],
                #                 [1, 3]]])

data[:, 0:2]    # Output: array([[[ 3,  1,  2],
                #                 [ 1,  0,  5]],
                #                [[ 5,  4,  3],
                #                 [ 1,  3, -3]]])

data[:, :, 0:2] # Output: array([[[3, 1],
                #                 [1, 0]],
                #                [[5, 4],
                #                 [1, 3]]])


#==============================================
# assigning to a slice expression assigns to the whole selection
arr_2d[:, :1] = 0
arr_2d

#======================================================
# 練習: 比較 arr_2d[:2,1:] 與 arr_2d[:2][1:] 的差異
arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
