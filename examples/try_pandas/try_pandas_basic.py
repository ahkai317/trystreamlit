# -*- coding: utf-8 -*-
import pandas as pd

#======================================================
# Pandas 基本簡介
#------------------------------------------------
# Series 單維度資料
# 類似 excel 的直向欄位資料，以 list 建立

data = pd.Series([1, 2, 3]) # Output: 0    1
                            #         1    2
                            #         2    3
                            #         dtype: int64

data.max()
print("最大值：", data.max())       # Output: 3

data.median()
print("中位數：", data.median())    # Output: 2.0

data * 2
print("資料放大(x2)：", data * 2)   # Output: 0    2
                                  #         1    4
                                  #         2    6
                                  #         dtype: int64

data = data == 2
print("比較運算(布林遮罩)：", data = data == 20)    # Output: 0    False
                                                 #         1     True
                                                 #         2    False
                                                 #         dtype: bool

print("遮罩後相乘：", data * 2)                    # Output: 0    False
                                                 #         1     True
                                                 #         2    False
                                                 #         dtype: bool

#------------------------------------------------
# DataFrame 雙維度資料
# 像 table，有 column & row 的概念，以 dict 建立

data = pd.DataFrame({
    "name": ["Amy", "John", "Bob"],
    "salary": [30000, 50000, 40000]
})
print(data) # Output:    name  salary
            #         0   Amy   30000
            #         1  John   50000
            #         2   Bob   40000

# 取得直向資料 by column name
data['salary']  # Output: 0    30000
                #         1    50000
                #         2    40000
                #         Name: salary, dtype: int64

# 取得橫向資料 by row name
data.iloc[0]    # Output: name        Amy
                #         salary    30000
                #         Name: 0, dtype: object
