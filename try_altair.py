# -*- coding: utf-8 -*-
import pandas as pd
import altair as alt
import streamlit as st

#======================================================
# 基本
#------------------------------------------------
# 數據
# 通常數據集會餵 DataFrame
# 繪圖圖表， labeled columns 需要指定的
data = pd.DataFrame({
    'a': list('CCCDDDEEE'),
    'b': [2, 7, 4, 1, 2, 6, 8, 4, 7]
})

# 帶入資料
chart = alt.Chart(data)

# 圖表物件
chart = alt.Chart(data).mark_point()
st.altair_chart(chart)


#======================================================
# 圖表物件
#------------------------------------------------
# 編碼 & 標記
# 為了直觀地分離點，達到有效的視覺化：
# 可以將各種 Encoding Channel (Channel)，mapping 到 `data` 中的 columns

# 例如：用 Channel 對 `data` 的 變數 進行 encode，Channel 表示各點的 x 軸位置
# 分離出 x 軸
alt.Chart(data).mark_point().encode(
    x='a',
)

# 截至目前，已分隔資料成一維的圖表，但 對於圖表縱軸，仍然有多個點重疊
# 讓我們進一步將這些分開：

# 新增 encoding channel，mapping 到 column：
# 分離出 y 軸
alt.Chart(data).mark_point().encode(
    x='a',
    y='b'
)

#------------------------------------------------
# 數學方法

# 用內建統計語法，取得平均值
# 將 y 軸替換成原本的平均值，並配合平均值，轉換標記為長條圖
alt.Chart(data).mark_bar().encode(
    x='a',
    y='average(b)'
)

#------------------------------------------------
# 軸向置換
alt.Chart(data).mark_bar().encode(
    y='a',
    x='average(b)'
)
#======================================================
# 檢視 JSON 輸出
#------------------------------------------------
# 導出並作為 JSON 發送給 Vega-Lite
chart = alt.Chart(data).mark_bar().encode(
    x='a',
    y='average(b)',
)
print(chart.to_json()) # 檢查 Altair 導出並作為 JSON 發送給 Vega-Lite 的 JSON 規範

# Output:
# 此處已擴展為 JSON 結構，並包括 "encoding" 字段。
'''
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.6.1.json",
  "config": {
    "view": {
      "continuousHeight": 300,
      "continuousWidth": 300
    }
  },
  "data": {
    "name": "data-347f1284ea3247c0f55cb966abbdd2d8"
  },
  "datasets": {
    "data-347f1284ea3247c0f55cb966abbdd2d8": [
      {
        "a": "C",
        "b": 2
      },
      {
        "a": "C",
        "b": 7
      },
      {
        "a": "C",
        "b": 4
      },
      {
        "a": "D",
        "b": 1
      },
      {
        "a": "D",
        "b": 2
      },
      {
        "a": "D",
        "b": 6
      },
      {
        "a": "E",
        "b": 8
      },
      {
        "a": "E",
        "b": 4
      },
      {
        "a": "E",
        "b": 7
      }
    ]
  },
  "encoding": {
    "x": {
      "field": "a",
      "type": "nominal"
    },
    "y": {
      "aggregate": "average",
      "field": "b",
      "type": "quantitative"
    }
  },
  "mark": {
    "type": "bar"
  }
}
'''

#------------------------------------------------
# Altair 簡化語法：指定 column 類別
y = alt.Y('average(b):Q')
print(y.to_json())
# Output:
'''
{
  "aggregate": "average",
  "field": "b",
  "type": "quantitative"
}
'''

#======================================================
# 自訂視覺化效果
#------------------------------------------------
# 預設情況下，Altair 通過對 Vega-Lite 預設屬性，可進行一些視覺化效果的選擇

# 換用 Altair 的 API 功能進行調整：
# - 調整軸向標題
# - 調整圖表顏色
test_chart = alt.Chart(data).mark_bar(color='firebrick').encode(
    alt.Y('a', title='category'),
    alt.X('average(b)', title='avg(b) by category')
)
st.altair_chart(test_chart)

#======================================================
# 發布視覺化資料
# vega-embed JS: https://github.com/vega/vega-embed
#------------------------------------------------

# 資料視覺化後，可以使用 Vega-Embed Javascript 直接完成，詳情參考上述 Github 網址

# 輸出 HTML 範本
chart = alt.Chart(data).mark_bar().encode(
    x='a',
    y='average(b)',
)
chart.save('./data/chart.html')

# 輸出後 HTML 範本 如下：
# JSON 規範 應會存入 JavaScript 的 `spec` 參數中

'''
<!DOCTYPE html>
<html>
<head>
  <style>
    .error {
        color: red;
    }
  </style>
  <script type="text/javascript" src="https://cdn.jsdelivr.net/npm//vega@5"></script>
  <script type="text/javascript" src="https://cdn.jsdelivr.net/npm//vega-lite@4.17.0"></script>
  <script type="text/javascript" src="https://cdn.jsdelivr.net/npm//vega-embed@6"></script>
</head>
<body>
  <div id="vis"></div>
  <script>
    (function(vegaEmbed) {
      var spec = {"data": {"name": "data-347f1284ea3247c0f55cb966abbdd2d8"}, "mark": "bar", "encoding": {"x": {"field": "a", "type": "nominal"}, "y": {"aggregate": "average", "field": "b", "type": "quantitative"}}, "$schema": "https://vega.github.io/schema/vega-lite/v4.17.0.json", "datasets": {"data-347f1284ea3247c0f55cb966abbdd2d8": [{"a": "C", "b": 2}, {"a": "C", "b": 7}, {"a": "C", "b": 4}, {"a": "D", "b": 1}, {"a": "D", "b": 2}, {"a": "D", "b": 6}, {"a": "E", "b": 8}, {"a": "E", "b": 4}, {"a": "E", "b": 7}]}};
      var embedOpt = {"mode": "vega-lite"};

      function showError(el, error){
          el.innerHTML = ('<div class="error" style="color:red;">'
                          + '<p>JavaScript Error: ' + error.message + '</p>'
                          + "<p>This usually means there's a typo in your chart specification. "
                          + "See the javascript console for the full traceback.</p>"
                          + '</div>');
          throw error;
      }
      const el = document.getElementById('vis');
      vegaEmbed("#vis", spec, embedOpt)
        .catch(error => showError(el, error));
    })(vegaEmbed);

  </script>
</body>
</html>
'''
