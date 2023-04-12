# -*- coding: utf-8 -*-

import time

import streamlit as st
import numpy as np
import pandas as pd
import emoji as emo

# CONFIG
st.set_page_config(
    page_title = "Try Streamlit | Streamlit",
    page_icon = ':thumb_up:',
    layout = "centered",
    initial_sidebar_state = "collapsed",
)

def space(rows) -> int:
    for i in range(rows):
        st.write('')
    return

# CONTENT
# 標題 H1
st.title("Try Streamlit")

# 表格
try_df = pd.DataFrame(
    {
        'Col 1': [1, 2, 3, 4],
        'Col 2': [10, 20, 30, 40]
    }
)

st.write("Create DataFrame：", try_df) # ex.表格

space(1)

# 圖表
try_chart_data = pd.DataFrame(
    np.random.randn(20, 3), # 隨機數值的二維 numpy.ndarray
    columns = ['a', 'b', 'c'],
)

st.write("Create Some Random Chart：")
st.line_chart(try_chart_data)
st.bar_chart(try_chart_data)
st.altair_chart(try_chart_data)
st.area_chart(try_chart_data)
# st.bokeh_chart(try_chart_data)
# st.plotly_chart(try_chart_data)
# st.pydeck_chart(try_chart_data)
# st.graphviz_chart(try_chart_data)
# st.vega_lite_chart(try_chart_data)
st._arrow_bar_chart(try_chart_data)
st._legacy_line_chart(try_chart_data)

space(1)

# 地圖 & 選單
try_map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [22.7, 120.3],
    columns=['lat', 'lon']
)

if st.checkbox('Show Map Chart'):
    st.write("Create Random Dot on Map：")
    st.map(try_map_data)

space(1)

# 下拉選單 & 內容寫入 Side Bar
st.write('Create Select Box：')

if not st.checkbox('Option go Side Bar'):
    option = st.selectbox(
        '你喜歡哪種動物？',
        ['狗', '貓', '鸚鵡', '天竺鼠']
    )
    st.write('你的答案：', option)
else:
    option = st.sidebar.selectbox(
        '你喜歡哪種動物？',
        ['狗', '貓', '鸚鵡', '天竺鼠']
    )
    st.write('你的答案：', option)

space(1)

# 並列
left_column, right_column = st.columns(2)
left_column.write("這是左邊欄位")
right_column.write("這是右邊欄位")

space(1)

# Toggle 效果
expander = st.expander("Try Toggle Effect")
expander.write("如果你要顯示很多文字，但又不想佔大半空間，可以使用這種方式。")

space(1)

# 進度條
latest_iteration = st.empty() # 增加一個空白元件 (DeltaGenerator)，等等要放文字
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f'目前進度 {i+1} %')
    bar.progress(i + 1)
    time.sleep(0.01)

space(1)

# Cache (以達同步渲染，不需重整網頁)
@st.cache(suppress_st_warning = True)
def expensive_computation(a):
    st.write(f"沒有快取：expensive_computation({a})")
    time.sleep(2)
    return a * 2

a = st.slider("選擇一個數字", 0, 10)
result = expensive_computation(a)
st.write("平方結果：", result)

space(3)


# 官方資源
cheat_sheet = 'https://share.streamlit.io/daniellewisdl/streamlit-cheat-sheet/app.py'
st.write(f'Offical Cheat Sheet：{cheat_sheet}')
st.write('Support by Streamlit')