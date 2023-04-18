# -*- coding: utf-8 -*-
import numpy as np

#======================================================
# 切割操作

#------------------------------------------------
# Case 1:

arr = np.arange(1, 9).reshape(2, 4) # Output: array([[1, 2, 3, 4],
                                    #                [5, 6, 7, 8]])
                                    # Shape: 2x4

# 根據第一維度切割
result = np.vsplit(arr, 2)  # Output: [array([[1, 2, 3, 4]]), array([[5, 6, 7, 8]])]
                            # 兩陣列，Shape: (2/2) x 4

# 根據第二維度切割
result = np.hsplit(arr, 2)  # Output: [array([[1, 2],
                            #                 [5, 6]]),
                            #          array([[3, 4],
                            #                 [7, 8]])]
                            # 兩陣列，Shape: 2 x (4/2)

#------------------------------------------------
# Case 2:

arr = np.array([        # Shape: 2x6
    [2, 4, 6, 8, 10, 12],
    [1, 3, 5, 7, 9, 11]
])

# 根據第一維度切割
result = np.vsplit(arr, 2)  # Output: [array([[2, 4, 6, 8, 10, 12]), array([[1, 3, 5, 7, 9, 11]])]
                            # 兩陣列，Shape: (2/2) x 6

# 根據第二維度切割
result = np.hsplit(arr, 2)  # Output: [array([[2, 4, 6],
                            #                 [1, 3, 5]]),
                            #          array([[8, 10, 12],
                            #                 [7, 9, 11]])]
                            # 兩陣列，Shape: 2 x (6/2)

# 根據第二維度切割成 3 陣列
result = np.hsplit(arr, 3)  # Output: [array([[2, 4],
                            #                 [1, 3]]),
                            #          array([[6, 8],
                            #                 [5, 7]]),
                            #          array([[9, 12],
                            #                 [9, 11]])]
                            # 三陣列，Shape: 2 x (6/3)