# -*- coding: utf-8 -*-
import pandas as pd

#======================================================
# Series 單維度資料
#------------------------------------------------
# 資料索引
# 每個資料的獨立編號，如 excel 最左邊的縱向的每條 row 編號

# 自訂索引 (平時為預設)
data = pd.Series([5, 4, -2, 3, 7], index = ["a", "b", "c", "d", "e"])

# 觀察資料
print("資料型態：", data.dtype) # 資料型態： int64
print("資料大小：", data.size)  # 資料大小： 5
print("資料索引：", data.index) # 資料索引： Index(['a', 'b', 'c', 'd', 'e'], dtype='object')

# 取得資料
print(data[2], data[0])     # 根據順序，Output: -2 5
print(data["e"], data["d"]) # 根據索引，Output: 7 3


#------------------------------------------------
# 數字 & 統計 運算

n = 2

# 基本
print("總和：", data.sum())         # 總和： 17
print("最大值：", data.max())       # 最大值： 7
print("乘法總和：", data.prod())    # 乘法總和： -840

# 統計
print("算數平均數：", data.mean())  # 算數平均數： 3.4
print("中位數：", data.median())    # 中位數： 4.0
print("標準差：", data.std())       # 標準差： 3.361547262794322

# 順序
print(f"前{n}大的數字：", data.nlargest(n))     # 前2大的數字： e    7
                                              #             a    5
                                              #             dtype: int64

print(f"取最小的{n}個數：", data.nsmallest(n))  # 取最小的2個數： c   -2
                                              #              d    3
                                              #              dtype: int64


#------------------------------------------------
# 字串操作
# 各種字串操作，皆定義於 pandas.str 下

data = pd.Series(["您好", "Python", "Pandas"])

# 基本
# 此處 Output 型別 -> pandas.core.series.Series
print("小寫化：", data.str.lower())
print("大寫化：", data.str.upper())
print("字串長：", data.str.len())

# 串接
cma_str = ','
print(f"將字串結合，每個元素中間以 {cma_str} 分開：\n{data.str.cat(sep = cma_str)}") # Output 型別 -> str

# 搜尋
upper_p_str = 'P'
print(f"找出包含 {upper_p_str} 的資料：\n{data.str.contains(upper_p_str)}") # Output 為布林遮罩 -> pandas.core.series.Series

# 取代
numpy_str = 'Numpy'
print(f"將 {data[0]} 變成 {numpy_str}：\n{data.str.replace(data[0], numpy_str)}")
