# -*- coding: utf-8 -*-
'''
實作目標：
    依各大廳遊戲為主體，以 4/1 ~ 4/12 的 大廳遊戲投注統計數據，做資料清洗、視覺化，與分析

方向：
1. 每個遊戲的統計數據比較
    使用長條圖或圓餅圖，將每個遊戲的投注玩家數量、注單數量、投注額、有效投注額、派彩、JP獎金等資料進行比較，找出投注量較大的遊戲。

2. 損益分析
    使用線圖來呈現公司損益的變化趨勢，找出收益較好或損失較大的遊戲類型。

3. RTP 與中獎率的分析
    使用散佈圖或氣泡圖，將 RTP 與中獎率進行比較，找出表現較好或較差的遊戲。

4. 平均有效投注額的分析
    使用直方圖或箱形圖，將平均有效投注額進行分析，找出投注金額偏高或偏低的遊戲。

綜合上述，也可以使用互動式圖表來進行更直觀的分析與比較。
'''

import streamlit as st
import altair as alt
import numpy as np
import pandas as pd
import emoji as emo
from decimal import Decimal

import time
import json
# from trystreamlit import model

def main():
#======================================================
# CONFIG
    st.set_page_config(
        page_title = "Lobby Game Data | Try Streamlit",
        page_icon = ':thumb_up:',
        layout = "centered",
        initial_sidebar_state = "collapsed",
    )
#======================================================
# 資料
# 4/1 ~ 4/12 Dev 的 大廳遊戲投注統計數據
    total = 15

    data = pd.DataFrame({
        # "Title": ['10021', '10005', '10016', '10001', '10010', '10003', '10011', '10009', '10012', '10014', '10008', '10004', '10002', '10006', '10007'],
        "PlayerCount": [9, 5, 1, 56, 5, 4, 6, 2, 5, 4, 4, 3, 2, 2, 2],
        "BetCount": [2936, 1894, 1426, 1343, 145, 141, 127, 70, 69, 30, 27, 14, 12, 11, 11],
        "Bet": ['2163525000', '105826840000', '284800020000', '209208560', '12907068000', '517975000', '14440530000', '2232030000', '10405320000', '2548090000', '1773630000', '801970000', '15080000', '601260000', '26290000'],
        "ValidBet": ['2163525000', '105826840000', '284800020000', '209208560', '12907068000', '517630000', '14440530000', '2232030000', '10405320000', '2548090000', '1773630000', '801970000', '15080000', '601260000', '26290000'],
        "GameWin": ['2141337200', '665346381600', '280770362000', '73438720', '230785644950', '3983332500', '109797721500', '87178631000', '15479736000', '11351527500', '29229275000', '4405950000', '70178200', '1703449000', '27422000'],
        "JPWin": ['93525335', '5512314727350', '64903200000', '7699548', '225620934', '3001380', '119493959400', '28642964000', '50079200350', '11214800000', '250033000000', '0', '18850000', '12300000', '40000'],
        "CompanyProfit": ['-71337535', '-6071834268950', '-60873542000', '128070292', '-218104197884', '-3468703880', '-214851150900', '-113589565000', '-55153616350', '-20018237500', '-277488645000', '-3603980000', '-73948200', '-1114489000', '-1172000'],
        "Odds": ['33.07', '34.64', '37.03', '34.18', '52.41', '19.86', '66.93', '91.43', '40.58', '90', '74.07', '50', '66.67', '72.73', '45.45'],
        "RTP": ['103.29', '5837.51', '121.37', '38.78', '1789.8', '770.11', '1587.83', '5189.06', '630.05', '885.61', '15745.23', '549.39', '590.37', '285.35', '104.45'],
        "AvgValidBet": ['736895', '55874783', '199719509', '155777', '89014262', '3671134', '113704960', '31886142', '150801739', '84936333', '65690000', '57283571', '1256666', '54660000', '2390000']
    }, index=['10021', '10005', '10016', '10001', '10010', '10003', '10011', '10009', '10012', '10014', '10008', '10004', '10002', '10006', '10007'])

    summary = pd.DataFrame({
        "PlayerCount": [74],
        "BetCount": [8256],
        "Bet": ["439268836560"],
        "ValidBet": ["439268491560"],
        "GameWin": ["1442344387170"],
        "JPWin": ["6037042888297"],
        "CompanyProfit": ["-7040118783907"],
        "AvgValidBet": ["53205970"]
    }, index=["Totle"])

    # 資料清洗
    for i in data.columns:
        if data[i].dtype == 'object':
            data[i] = data[i].astype(float)

    for i in summary.columns:
        if summary[i].dtype == 'object':
            summary[i] = summary[i].astype(float)

    np.set_printoptions(precision=4)

#======================================================
# 頁面呈現
#------------------------------------------------
    # Sidebar
    st.sidebar.button('Hit me')
    st.sidebar.download_button('On the dl', data.to_csv().encode('utf-8'), mime='text/csv')
    st.sidebar.checkbox('Check me out')
    st.sidebar.radio('Radio', [1,2,3])
    st.sidebar.selectbox('Select', [1,2,3])
    st.sidebar.multiselect('Multiselect', [1,2,3])
    st.sidebar.slider('Slide me', min_value=0, max_value=10)
    st.sidebar.select_slider('Slide to select', options=[1,'2'])
    st.sidebar.text_input('Enter some text')
    st.sidebar.number_input('Enter a number')
    st.sidebar.text_area('Area for textual entry')
    st.sidebar.date_input('Date input')
    st.sidebar.time_input('Time entry')
    st.sidebar.file_uploader('File uploader')
    # st.sidebar.camera_input("一二三,茄子!")
    st.sidebar.color_picker('Pick a color')

    st.sidebar.button('統計數據比較')


    #------------------------------------------------
    # Body
    st.title("Try Streamlit")   # H1

    st.text('報表 > 大廳遊戲投注統計 > 遊戲')
    st.divider()    # 分隔線

    # 總計
    with st.container():
        st.subheader('總計')    # H2

        st.empty()
        # 總計統計表
        st.write(summary)

    st.divider()    # 分隔線

    # 大廳遊戲
    with st.container():
        st.subheader('大廳遊戲')    # H3
        # 圖表位置 (長條圖)
        # TODO: 完成其他圖表
        # check_player_count = st.checkbox('投注玩家數量')
        # check_bet_count = st.checkbox('注單數量')
        # check_bet = st.checkbox('投注額')
        # check_valid_bet = st.checkbox('有效投注額')
        # check_game_win = st.checkbox('派彩')
        # check_jp_win = st.checkbox('JP獎金')

        get_lobby_game_line_chart()

    # 損益分析表
    profit_n_loss_analysis()

    # 各個遊戲 RTP：散佈圖
    rtp_n_game_win_analysis()

    # 平均有效投注：箱形圖
    avg_valid_bet_analysis()

    # 各個遊戲資料表格
    detail_list_table()

    return


#======================================================
# CONFIG
st.set_page_config(
    page_title = "Lobby Game Data | Try Streamlit",
    page_icon = ':thumb_up:',
    layout = "centered",
    initial_sidebar_state = "collapsed",
)

#======================================================
# 取得資料

# DB 取後清洗

# Json 轉譯清洗
# data = model.lobby_game_list_april.Get_Game_Stat_Data()
# data = json.loads(data)
# pd.json_normalize(data)

# .py 靜態設定取用
# totle, data, summary = model.lobby_game_list_april.get_Game_Stat_Data()

total = 15

data = pd.DataFrame({
    # "Title": ['10021', '10005', '10016', '10001', '10010', '10003', '10011', '10009', '10012', '10014', '10008', '10004', '10002', '10006', '10007'],
    "PlayerCount": [9, 5, 1, 56, 5, 4, 6, 2, 5, 4, 4, 3, 2, 2, 2],
    "BetCount": [2936, 1894, 1426, 1343, 145, 141, 127, 70, 69, 30, 27, 14, 12, 11, 11],
    "Bet": ['2163525000', '105826840000', '284800020000', '209208560', '12907068000', '517975000', '14440530000', '2232030000', '10405320000', '2548090000', '1773630000', '801970000', '15080000', '601260000', '26290000'],
    "ValidBet": ['2163525000', '105826840000', '284800020000', '209208560', '12907068000', '517630000', '14440530000', '2232030000', '10405320000', '2548090000', '1773630000', '801970000', '15080000', '601260000', '26290000'],
    "GameWin": ['2141337200', '665346381600', '280770362000', '73438720', '230785644950', '3983332500', '109797721500', '87178631000', '15479736000', '11351527500', '29229275000', '4405950000', '70178200', '1703449000', '27422000'],
    "JPWin": ['93525335', '5512314727350', '64903200000', '7699548', '225620934', '3001380', '119493959400', '28642964000', '50079200350', '11214800000', '250033000000', '0', '18850000', '12300000', '40000'],
    "CompanyProfit": ['-71337535', '-6071834268950', '-60873542000', '128070292', '-218104197884', '-3468703880', '-214851150900', '-113589565000', '-55153616350', '-20018237500', '-277488645000', '-3603980000', '-73948200', '-1114489000', '-1172000'],
    "Odds": ['33.07', '34.64', '37.03', '34.18', '52.41', '19.86', '66.93', '91.43', '40.58', '90', '74.07', '50', '66.67', '72.73', '45.45'],
    "RTP": ['103.29', '5837.51', '121.37', '38.78', '1789.8', '770.11', '1587.83', '5189.06', '630.05', '885.61', '15745.23', '549.39', '590.37', '285.35', '104.45'],
    "AvgValidBet": ['736895', '55874783', '199719509', '155777', '89014262', '3671134', '113704960', '31886142', '150801739', '84936333', '65690000', '57283571', '1256666', '54660000', '2390000']
}, index=['10021', '10005', '10016', '10001', '10010', '10003', '10011', '10009', '10012', '10014', '10008', '10004', '10002', '10006', '10007'])

summary = pd.DataFrame({
    "PlayerCount": [74],
    "BetCount": [8256],
    "Bet": ["439268836560"],
    "ValidBet": ["439268491560"],
    "GameWin": ["1442344387170"],
    "JPWin": ["6037042888297"],
    "CompanyProfit": ["-7040118783907"],
    "AvgValidBet": ["53205970"]
}, index=["Totle"])

# 資料清洗
for i in data.columns:
    if data[i].dtype == 'object':
        data[i] = data[i].astype(float)

for i in summary.columns:
    if summary[i].dtype == 'object':
        summary[i] = summary[i].astype(float)

np.set_printoptions(precision=4)

#======================================================
# Func
#------------------------------------------------
# 每個遊戲的數據比較 (直方圖)
def get_lobby_game_line_chart():
    # 直方表選擇
    col, col2, col3 = st.columns(3)

    check_player_count = col.checkbox('投注玩家數量', value=True)
    check_valid_bet = col.checkbox('有效投注額')
    check_bet_count = col2.checkbox('注單數量')
    check_game_win = col2.checkbox('派彩')
    check_bet = col3.checkbox('投注額')
    check_jp_win = col3.checkbox('JP獎金')

    chart_str = ''

    if check_player_count:
        chart_str = 'PlayerCount'
    elif check_bet_count:
        chart_str = 'BetCount'
    elif check_bet:
        chart_str = 'Bet'
    elif check_valid_bet:
        chart_str = 'ValidBet'
    elif check_game_win:
        chart_str = 'GameWin'
    elif check_jp_win:
        chart_str = 'JPWin'

    st.bar_chart(data[chart_str].to_frame())
    # # 定義CSS樣式
    # css = """
    #     .stChVl g rect {
    #         fill: red;
    #         opacity: 0.7;
    #     }
    # """

    # # 將CSS樣式應用於Streamlit
    # st.write(f'<style>{css}</style>', unsafe_allow_html=True)

#------------------------------------------------
# 損益分析
def profit_n_loss_analysis():
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
def rtp_n_game_win_analysis():
    # chart_data = pd.DataFrame(
    # np.random.randn(20, 3),
    # columns=['a', 'b', 'c'])

    chart = alt.Chart(data.reset_index(names="GameCode")).mark_circle(opacity=0.7).encode(
        x='RTP', # 不設定時，預設為變量 'RTP:Q'
        y='GameCode:N',
        size=alt.Size('RTP', scale=alt.Scale(range=[40, 1000]), legend=None),
        color=alt.Color('GameCode', type='ordinal', scale=alt.Scale(scheme='purplered'), legend=alt.Legend(title='GameCode')),
        tooltip=['RTP', 'GameCode']
    )

    st.altair_chart(chart, use_container_width=True, theme='streamlit')


#------------------------------------------------
# 平均有效投注額分析
def avg_valid_bet_analysis():
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
def detail_list_table():
    # 全部遊戲統計表
    if not st.checkbox('隱藏靜態表格', value=True):
        st.write(data)  # 動態表格
        st.table(data)  # 靜態表格
    else:
        st.write(data)  # 動態表格


#======================================================
# 頁面呈現
#------------------------------------------------
# Sidebar
st.sidebar.button('Hit me')
st.sidebar.download_button('On the dl', data.to_csv().encode('utf-8'), mime='text/csv')
st.sidebar.checkbox('Check me out')
st.sidebar.radio('Radio', [1,2,3])
st.sidebar.selectbox('Select', [1,2,3])
st.sidebar.multiselect('Multiselect', [1,2,3])
st.sidebar.slider('Slide me', min_value=0, max_value=10)
st.sidebar.select_slider('Slide to select', options=[1,'2'])
st.sidebar.text_input('Enter some text')
st.sidebar.number_input('Enter a number')
st.sidebar.text_area('Area for textual entry')
st.sidebar.date_input('Date input')
st.sidebar.time_input('Time entry')
st.sidebar.file_uploader('File uploader')
# st.sidebar.camera_input("一二三,茄子!")
st.sidebar.color_picker('Pick a color')

st.sidebar.button('統計數據比較')


#------------------------------------------------
# Body
st.title("Try Streamlit")   # H1

st.text('報表 > 大廳遊戲投注統計 > 遊戲')
st.divider()    # 分隔線

# 總計
with st.container():
    st.subheader('總計')    # H2

    st.empty()
    # 總計統計表
    st.write(summary)

st.divider()    # 分隔線

# 大廳遊戲
with st.container():
    st.subheader('大廳遊戲')    # H3
    # 圖表位置 (長條圖)
    # TODO: 完成其他圖表
    # check_player_count = st.checkbox('投注玩家數量')
    # check_bet_count = st.checkbox('注單數量')
    # check_bet = st.checkbox('投注額')
    # check_valid_bet = st.checkbox('有效投注額')
    # check_game_win = st.checkbox('派彩')
    # check_jp_win = st.checkbox('JP獎金')

    get_lobby_game_line_chart()

# 損益分析表
profit_n_loss_analysis()

# 各個遊戲 RTP：散佈圖
rtp_n_game_win_analysis()

# 平均有效投注：箱形圖
avg_valid_bet_analysis()

# 各個遊戲資料表格
detail_list_table()


if __name__ == "__main__":
    main()