# -*- coding: utf-8 -*-
import numpy as np

#======================================================
# 合併操作

#------------------------------------------------
# Case 1:
# 兩陣列， Shape: 1x2
arr = np.array([
    [3, 4]
])

arr2 = np.array([
    [5, 6]
])

# 合併第一維度
result = np.vstack((arr, arr2)) # Output: array([[3, 4],
                                #                [5, 6]])
                                # Shape: (1+1) x 2

# 合併第二維度
result2 = np.hstack((arr, arr2))    # Output: array([[3, 4, 5, 6]])
                                    # Shape: 1 x (2+2)

#------------------------------------------------
# Case 2:
# 兩陣列， Shape: 2x3
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

arr2 = np.array([
    [7, 8, 9],
    [10, 11, 12]
])

# 合併第一維度
result = np.vstack((arr, arr2)) # Output: array([[ 1,  2,  3],
                                #                [ 4,  5,  6],
                                #                [ 7,  8,  9],
                                #                [10, 11, 12]])
                                # Shape: (2+2) x 3

# 合併第二維度
result2 = np.hstack((arr, arr2))    # Output: array([[ 1,  2,  3,  7,  8,  9],
                                    #                [ 4,  5,  6, 10, 11, 12]])
                                    # Shape: 2 x (3+3)

#------------------------------------------------
# Case 3:
# 兩陣列， Shape: 2x3，和一陣列，Shape: 2x2

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

arr2 = np.array([
    [7, 8, 9],
    [10, 11, 12]
])

arr3 = np.array([
    [13, 14],
    [15, 16]
])

# 第二維度未對齊，無法合併第一維度

# 合併第二維度
result2 = np.hstack((arr, arr2, arr3))  # Output: array([[ 1,  2,  3,  7,  8,  9, 13, 14],
                                        #                [ 4,  5,  6, 10, 11, 12, 15, 16]])
                                        # Shape: 2 x (3+3+2)