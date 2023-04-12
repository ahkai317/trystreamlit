# -*- coding: utf-8 -*-
import pandas as pd

#======================================================
# 篩選資料
#------------------------------------------------
# 基本邏輯 (以 Series 舉例)

data = pd.Series([1, 2, 3]) # Output: 0    1
                            #         1    2
                            #         2    3
                            #         dtype: int64

# 建立篩選條件 (布林遮罩)
cond = [True, False, True]

# 過濾資料
filteredData = data[cond]   # Output: 0    1
                            #         2    3
                            #         dtype: int64


#------------------------------------------------
# 常見操作 - Series
# Case 1: 數值處理
data = pd.Series([30, 15, 20])  # Output: 0    30
                                #         1    15
                                #         2    20
                                #         dtype: int64

# 以篩選條件建立布林遮罩
cond = data > 18

# 遮罩過濾資料
filteredData = data[cond]       # Output: 0    30
                                #         2    20
                                #         dtype: int64

# Case 2: 字串處理
data = pd.Series(['Numpy', 'Python', 'Pandas'])

# 陣列內字串之中有包含 'P'
cond = data.str.contains('P')

# 遮罩過濾資料
filteredData = data[cond]   # Output: 1    Python
                            #         2    Pandas
                            #         dtype: object

#------------------------------------------------
# 常見操作 - DataFrame

data = pd.DataFrame({
    "name": ["Amy", "John", "Bob"],
    "salary": [30000, 50000, 40000]
})
print(data)

# 以篩選條件建立 布林遮罩 (型別: Series，對欄位資料判別)
cond = data["salary"] >= 40000
print(cond)                 # Output: 0    False
                            #         1     True
                            #         2     True
                            #         dtype: bool

# 遮罩過濾資料
filteredData = data[cond]   # Output:    name  salary
                            #         1  John   50000
                            #         2   Bob   40000