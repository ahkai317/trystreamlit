# -*- coding: utf-8 -*-
import numpy as np

#======================================================
# 多維陣列 N-Dimensional Arrray (ndarray)

# 建立陣列一個 維度(ndim) 為 3 的陣列
# 此陣列 形狀(Shape) 為 (2, 2, 3) -> ( 代表由最外層數至內，有 2(二維陣列)、2(一維陣列)、3(值) )
array_3d = np.array([
    [
        [5, 2, 4],
        [1, 2, 8]
    ], [
        [3, 8, 2],
        [4, 1, 3]
    ]
])


#======================================================
# 常用 Method

# 陣列建立
array = np.arange(0, 5) # 建立一含元素 0~5(offset) 的一維陣列
                        # Output: array([0, 1, 2, 3, 4])

array_2d = numpy.random.randn(1000, 2)  # 隨機建立一 Shape(1000, 2) 的 二維陣列

array_2d = np.random.randint(0, 2, (2, 3))  # 隨機建立一 範圍於 0~2(offset) 正整數 的 2x3 二維陣列
                                            # Output: array([[0, 0, 1],
                                            #                [1, 1, 1]])

array_3d_empty = np.empty([2, 2, 3]) # 元素皆為空 的 三維陣列 (Shape：2 x 2 x 3 )
array_2d_0 = np.zeros([3, 3])        # 元素皆為０ 的 二維陣列 (Shape：3 x 3 )
array_1d_1 = np.ones([4])            # 元素皆為１ 的 一維陣列 (Shape：4 )

# 查看維度
array.ndim      # Output: 1

# 查看 Shape
array.shape     # Output: (5,)
array_2d.shape  # Output: (2, 3) -> 代表此陣列為一 2x3 的陣列


#======================================================
# 一維陣列 One-Dimensional Array

arr_1d = np.arange(0, 10)

slice_24 = arr_1d[2:5] # 切片 [2][3][4], 為一個 view (會影響原陣列元素記憶體位置)
                       # Output: array([2, 3, 4])

# 變更 arr_1d 的值
arr_1d[2:4] = arr_1d[2:4] * 100

# 檢視 arr_1d
arr_1d # Output: array([  0,   1, 200, 300,   4,   5,   6,   7,   8,   9])

# 檢視 slice_24
slice_24 # Output: array([200, 300,   4])


#======================================================
# 二維陣列 Two-Dimensional Array

arr_2d = np.array(
    [
        [1, 2, 3], #     ------> axis 1 (第二軸)
        [4, 5, 6], #   /
        [7, 8, 9]  # Ｖ axis 0 (第一軸)
    ]
)
# arr_2d
# arr_2d.ndim
# arr_2d.shape
