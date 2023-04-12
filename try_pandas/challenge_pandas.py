# -*- coding: utf-8 -*-
import pandas as pd

#======================================================
# 資料集分析應用

# Google Play Store 資料集
# https://cwpeng.github.io/live-records-samples/data/googleplaystore.csv

#------------------------------------------------
# 讀取資料

data = pd.read_csv("./data/googleplaystore.csv")   # 已經在根目錄


#------------------------------------------------
# 觀察資料
print(data)

print("資料形狀：", data.shape)
print("資料欄位：", data.columns)


#------------------------------------------------
# 分析資料
# Case 1: 對 評分(Rating) 欄位進行分析

# 觀察資料
data["Rating"].dtype    # -> float64

print("平均數：", data["Rating"].mean())                             # 平均數： 4.193338315362443
print("中位數：", data["Rating"].median())                           # 中位數： 4.3
print("前一百個應用程式平均：", data["Rating"].nlargest(100).mean())    # 前一百個應用程式平均： 5.14

# 評分不應大於 5 分
# 尋找原因
cond = data["Rating"] > 5   # 建立布林遮罩篩選

print(data[cond])           # Output:
                            #                                            App  ... Android Ver
                            # 10472  Life Made WI-Fi Touchscreen Photo Frame  ...         NaN
                            #
                            # [1 rows x 13 columns]

print(data[cond]["Rating"]) # 19.0

# 排除資料
# 排除例外資料 (評分 19分)
cond = data["Rating"] <= 5

data = data[cond]

print("平均數：", data["Rating"].mean())                             # 平均數： 4.191757420456972
print("中位數：", data["Rating"].median())                           # 中位數： 4.3
print("前一百個應用程式平均：", data["Rating"].nlargest(100).mean())    # 前一百個應用程式平均： 5.0
print("前一千個應用程式平均：", data["Rating"].nlargest(1000).mean())   # 前一千個應用程式平均： 4.823


#------------------------------------------------
# 分析資料
# Case 2: 對 安裝數量(Installs) 統計各種數據

# 觀察資料
data["Installs"]                # 0            10,000+
                                # 1           500,000+
                                # 2         5,000,000+
                                # 3        50,000,000+
                                # 4           100,000+
                                #             ...
                                # 10834           500+
                                # 10836         5,000+
                                # 10837           100+
                                # 10839         1,000+
                                # 10840    10,000,000+
                                # Name: Installs, Length: 9366, dtype: object

data["Installs"].dtype          # -> dtype('O')
type(data["Installs"][0]) # -> str

# 轉換資料
# data["Installs"] = pd.to_numeric(data["Installs"])  # ValueError: Unable to parse string "10,000+" at position 0

# 因資料型態為字串，這邊轉換處理為數值
# 需把 逗號 & 加號 清理
# data["Installs"] = pd.to_numeric(data["Installs"].str.replace("[,+]", "")) # ValueError: Unable to parse string "Free" at position 10472

# 有例外資料 (data["Installs"][10472]字串值為 "Free")
data["Installs"] = pd.to_numeric(data["Installs"].str.replace("[,+]", "", regex=True).replace("Free", ""))

# 篩選資料
print("平均數：", data["Installs"].mean())  # 平均數： 17897443.726030324

cond = data["Installs"] > 10000
print("安裝數大於 10000 的應用程式數量：", data[cond].shape[0]) # 安裝數大於 10000 的應用程式數量： 6564



#======================================================
# 基於資料的應用
# Case: 關鍵字搜尋應用程式名稱

kwd = input("請輸入關鍵字：")

cond = data["App"].str.contains(kwd, case=False) # case 直接忽略大小寫

print(data[cond]["App"])
print("查詢結果應用數量總計：", data[cond]["App"].shape[0])

#------------------------------------------------
# 輸出資料
# 以最後範例輸出

data[cond].to_csv("./data/try_google_playstore_data.csv")
