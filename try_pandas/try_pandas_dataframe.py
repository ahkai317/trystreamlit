# -*- coding: utf-8 -*-
import pandas as pd

#======================================================
# DataFrame 雙維度資料
#------------------------------------------------
# 資料索引
# 每個資料的獨立編號，如 excel 最左邊的的每條 row 資料縱向編號

data = pd.DataFrame({
    "name": ["Amy", "Bob", "Charles"],
    "salary": [30000, 50000, 40000]
    },
    index=["a", "b", "c"]
)
# Output:
#       name  salary
# a      Amy   30000
# b      Bob   50000
# c  Charles   40000


# 觀察資料
print("資料數量：", data.size)                  # 資料數量： 6
print("資料形狀 (row, column)：", data.shape)   # 資料形狀 (row, column)： (3, 2)
print("資料索引：", data.index)                 # 資料索引： Index(['a', 'b', 'c'], dtype='object')


# 取得欄列資料
# 取完後會變單維度資料 (pandas.core.series.Series)

# 取得 row 資料
# 根據順序
print("取得第 2 列：", data.iloc[1], sep="\n")   # Output:
                                                # 取得第二列：
                                                # name        Bob
                                                # salary    50000
                                                # Name: b, dtype: object

# 根據索引
print("取得第 c 列：", data.loc["c"], sep="\n")  # Output:
                                                # 取得第 c 列：
                                                # name      Charles
                                                # salary      40000
                                                # Name: c, dtype: object



# 取得 column 資料
# 根據索引
print("取得 name 欄位，並將名字轉為大寫：", data["name"].str.upper(), sep="\n") # Output:
                                                                            # 取得 name 欄位，並將名字轉為大寫：
                                                                            # a        AMY
                                                                            # b        BOB
                                                                            # c    CHARLES
                                                                            # Name: name, dtype: object

print("取得薪水的平均值：", data["salary"].mean())  # 取得薪水的平均值： 40000.0


#------------------------------------------------
# 建立新欄位

# 以 list 建立
data["revenue"] = [500000, 400000, 300000]

# 以 Series 建立
data["rank"] = pd.Series([3, 6, 1], index=["a", "b", "c"])

# 以現有欄位產生新欄位，列如：CP值
data["cp"] = data["revenue"] / data["salary"]

print(data) # Output:
            #       name  salary  revenue  rank         cp
            # a      Amy   30000   500000     3  16.666667
            # b      Bob   50000   400000     6   8.000000
            # c  Charles   40000   300000     1   7.500000
