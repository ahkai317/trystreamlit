# -*- coding: utf-8 -*-
import streamlit as st

import time

#======================================================
# 基本
#------------------------------------------------
# 基本文本

st.title('Streamlit 的 Title(H1)')

st.header('Streamlit 的 header(H2)')

st.subheader('Streamlit 的 subheader(H3)')

st.text('Streamlit 的 text')

st.caption('Streamlit 的 caption')

st.markdown('### Streamlit 的 markdown')    # 特殊用法：https://docs.streamlit.io/library/api-reference/text/st.markdown

st.divider() # 分隔線

#------------------------------------------------
# 基本顯示
# write & text差異，在於 write 是依照內容直接顯示，如果是 code/script 也不會去執行它

st.header('write 顯示')

st.write(range(1, 100))

st.text(range(1, 100))

# Magic
# TODO: Magic


st.divider()

#------------------------------------------------
# 狀態物件

st.header('狀態物件')

st.success('Success!')

st.info('infomation')

st.warning('Warning!')

st.error('Error!')

st.exception(RuntimeError('This is an exception of type RuntimeError'))

#------------------------------------------------
# 動態狀態
# 進度條
progress_text = '流程進行中，請稍候...'
progress_bar = st.progress(0, text=progress_text)

for i in range(100):
    time.sleep(0.1)
    progress_bar.progress(i + 1, text=progress_text)

st.success('成功!')

# 等待條
with st.spinner(progress_text):
    time.sleep(5)
st.success('完成!')

# 效果
st.balloons()   # 氣球
st.snow()       # 雪花

st.divider()

#------------------------------------------------------------------
# 媒體物件

st.header('媒體物件')

st.image('./static/image/adoy_wonder.jpg', width=400, caption='Adoy - Wonder')  # 圖片
                                                                                # 如果使用 OpenCV，則需要將 BGR 轉為 RGB 才能正確顯示色彩

st.audio('./static/audio/adoy_wonder.mp3', format='audio/wav', start_time=2)    # 音訊
                                                                                # format 詳細：https://datatracker.ietf.org/doc/html/rfc4281

st.video('./static/video/adoy_wonder.mp4', format='video/mp4')  # 影像
