import streamlit as st
import altair as alt
import numpy as np
import pandas as pd
import emoji as emo
from decimal import Decimal

import time
import json
import sys
import os

from data import get_game_stat_total as ggst
from vega_datasets import data as d
# import trystreamlit
# from trystreamlit import model

#======================================================
# CONFIG
st.set_page_config(
    page_title = "Lobby Game Data | Try Streamlit",
    page_icon = ':thumb_up:',
    # layout = "centered",
    initial_sidebar_state = "collapsed",
)

#======================================================
# Func
#------------------------------------------------
# 每個遊戲的數據比較 (直方圖)
def get_lobby_game_line_chart(data):
    # 直方表選擇
    chart_str = st.selectbox('Select Game Kind:', data.columns[0:6])
    st.write('')

    st.bar_chart(data[chart_str].to_frame())

#------------------------------------------------
# 損益分析
def profit_n_loss_analysis(data):
    # 將row 加為為新的 column
    data_tmp = data.reset_index()

    chart = alt.Chart(data_tmp).mark_bar(opacity=0.8).encode(
        x=alt.X("index:N", axis=alt.Axis(title='Index')),
        y=alt.Y(
            "CompanyProfit:Q", axis=alt.Axis(title='Company Profit'),
            # y軸自動適應檢視範圍
            scale=alt.Scale(domain=(data_tmp['CompanyProfit'].min(), data_tmp['CompanyProfit'].min()*-1)),
        ),
        color=alt.condition(
            alt.datum.CompanyProfit > 0,
            alt.value("steelblue"), # The positive color
            alt.value("orange"),    # The negative color
        )
    )

    chart2 = alt.Chart(data_tmp).mark_line(point=True, opacity=0.7).encode(
        x=alt.X("index:N", axis=alt.Axis(title='Index')),
        y=alt.Y(
            "CompanyProfit:Q", axis=alt.Axis(title='Company Profit'),
            # y軸自動適應檢視範圍
            scale=alt.Scale(domain=(data_tmp['CompanyProfit'].min(), data_tmp['CompanyProfit'].min()*-1)),
        ),
        color=alt.value('aquamarine')
    )

    st.altair_chart(chart + chart2, use_container_width=True, theme='streamlit')



#------------------------------------------------
# RTP與中獎率分析
def rtp_n_game_win_analysis(data):

    brush = alt.selection_interval()

    chart = alt.Chart(data.reset_index(names="GameCode")).mark_circle(opacity=0.7).encode(
        x='RTP', # 不設定時，預設為變量 'RTP:Q'
        y='GameCode:N',
        size=alt.Size('RTP', scale=alt.Scale(range=[40, 1000]), legend=None),
        color=alt.Color('GameCode', type='ordinal', scale=alt.Scale(scheme='purplered'), legend=alt.Legend(title='GameCode')),
        tooltip=['RTP', 'GameCode']
    ).add_selection(
        brush
    )

    bars = alt.Chart(data.reset_index(names="GameCode")).mark_bar().encode(
        x='RTP',
        y='GameCode:N',
        color=alt.Color('GameCode', type='ordinal', scale=alt.Scale(scheme='purplered'), legend=alt.Legend(title='GameCode')),
        tooltip=['RTP', 'GameCode']
    ).transform_filter(
        brush
    )

    st.altair_chart(chart & bars)


#------------------------------------------------
# 平均有效投注額分析
def avg_valid_bet_analysis(data):
    chart = alt.Chart(data.reset_index(names="GameCode")).mark_bar(opacity=0.8).encode(
        x='GameCode:N',
        y='AvgValidBet',
        color=alt.Color(
            'GameCode',
            type='ordinal',
            scale=alt.Scale(scheme='bluepurple'),
            legend=None
        ),
    )

    chart2 = alt.Chart(data.reset_index(names="GameCode")).mark_line(opacity=0.7).encode(
        x='GameCode:N',
        y='AvgValidBet',
        color=alt.value('aquamarine')
    )

    st.altair_chart(alt.layer(chart, chart2), use_container_width=True, theme='streamlit')

#------------------------------------------------
# 主資料表格
def detail_list_table(data):
    col, col2, col3, col4 = st.columns(4)
    # 全部遊戲統計表
    if not col4.checkbox('隱藏靜態表格', value=True):
        st.write(data)  # 動態表格
        st.table(data)  # 靜態表格
    else:
        st.write(data)  # 動態表格

    col.download_button('下載CSV', data.to_csv().encode('utf-8'), mime='text/csv')


# Cache (以達同步渲染，不需重整網頁)
@st.cache(suppress_st_warning = True)
def expensive_computation(pic):
    if pic is not None:
        time.sleep(1)
        st.text('圖片預覽')
        st.image(pic)
    else:
        st.write("未上傳圖片")

#======================================================
# 取得資料
data = ggst.get_data()
summary = ggst.get_summary()

# 資料清洗
for i in data.columns:
    if data[i].dtype == 'object':
        data[i] = data[i].astype(float)

for i in summary.columns:
    if summary[i].dtype == 'object':
        summary[i] = summary[i].astype(float)

# np.set_printoptions(precision=4)

#======================================================
# 頁面呈現
#------------------------------------------------
# Sidebar
st.sidebar.write('sidebar')

#------------------------------------------------
# Body
st.title("Try Streamlit", )   # H1

st.text('報表 > 大廳遊戲投注統計 > 遊戲')
st.divider()    # 分隔線

# 總計
# test
# 將資料從寬表格轉為長表格
summary_long = pd.melt(summary.reset_index(), id_vars=["index"], var_name="metric", value_name="value")

# 定義顏色和圖例標籤
color_scale = alt.Scale(
    domain=["PlayerCount", "BetCount", "Bet", "ValidBet", "GameWin", "JPWin", "CompanyProfit", "AvgValidBet"],
    range=["#69c2ff", "#a7e6c7", "#f3e1f5", "#d4b9da", "#ffb347", "#f7cac9", "#a1cae2", "#f4d6cc"]
)
# legend_labels = {
#     "PlayerCount": "玩家數",
#     "BetCount": "投注筆數",
#     "Bet": "投注金額",
#     "ValidBet": "有效投注金額",
#     "GameWin": "遊戲獲利",
#     "JPWin": "大獎獲利",
#     "CompanyProfit": "公司獲利",
#     "AvgValidBet": "平均有效投注金額"
# }

# 繪製水平堆疊條形圖
bars = alt.Chart(summary_long).mark_bar().encode(
    x=alt.X("value:Q", title=None, axis=None, stack="zero"),
    y=alt.Y("index:N", title=None),
    color=alt.Color("metric:N", title=None, scale=color_scale, legend=alt.Legend(title=None, labelFontSize=12, labelLimit=300, labelPadding=10, labelOverlap=True, direction="horizontal", orient="top", symbolLimit=0, symbolType="circle"), sort=["PlayerCount", "BetCount", "Bet", "ValidBet", "GameWin", "JPWin", "CompanyProfit", "AvgValidBet"]),
    tooltip=[alt.Tooltip("metric:N", title="指標"), alt.Tooltip("value:Q", title="數值", format=",.0f")],
).properties(
    height=100
)

# 加上條形圖上的文字
text = bars.mark_text(
    align="center",
    baseline="middle",
    dx=0  # Nudges text to right so it doesn't appear on top of the bar
).encode(
    text=alt.Text("value:Q", format=",.0f"),
)
st.altair_chart(bars + text)
# test end

with st.container():
    st.subheader('總計')    # H2

    st.empty()
    # 總計統計表
    st.write(summary)

st.divider()    # 分隔線

# 大廳遊戲
st.subheader('大廳遊戲')    # H3

# 分頁看圖表分析
tab1, tab2, tab3, tab4 = st.tabs(["統計數據比較", "損益分析", "RTP 分析", "平均有效投注額分析"])

# 各個遊戲資料表格
detail_list_table(data)

# 統計數據分析
with tab1:
    with st.container():
        get_lobby_game_line_chart(data)


# 損益分析表
with tab2:
    profit_n_loss_analysis(data)

# 各個遊戲 RTP：散佈圖
with tab3:
    rtp_n_game_win_analysis(data)

# 平均有效投注：箱形圖
with tab4:
    avg_valid_bet_analysis(data)

#------------------------------------------------
# 聯絡我們

with st.expander('聯絡我們'):
    st.divider()
    st.write('')
    col, col2 = st.columns([2, 1])
    col.text_input('姓名：')
    col2.selectbox('性別：', ['', '男', '女', '其他'])
    st.date_input('生日：')
    st.text_input('電話：')
    st.text_input('E-mail：')

    st.text_input('請輸入您的主旨：')
    st.text_area('請輸入您的意見：')

    if st.checkbox('使用相機'):
        upd_pic = st.camera_input("一二三, 茄子！")
        expensive_computation(upd_pic)
    else:
        upd_pic = st.file_uploader('附件圖片上傳')
        expensive_computation(upd_pic)
