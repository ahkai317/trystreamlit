# -*- coding: utf-8 -*-

import streamlit as st
import numpy as np
import pandas as pd

from datetime import time
from datetime import datetime
from datetime import date

from io import StringIO

#========================================
# 輸入元件
#-------------------------------------------------------------------
# 按鈕
# st.button(label, key=None, help=None, on_click=None, args=None, kwargs=None, *, type="secondary", disabled=False, use_container_width=False)
# -> (bool)

if st.button('Hello', key=None, help=None, on_click=None, args=None, kwargs=None, type="secondary", disabled=False, use_container_width=False):
    st.write('Why hello there')
else:
    st.write('Goodbye')


# 實作 - 計數器

# # Case 1:
    # count = 0

    # if "count" not in st.session_state:
    #     st.session_state.count = count

    # if st.session_state.count < 3:
    #     if st.button("Click me!"):
    #         st.session_state.count += 1
    # else:
    #     st.button("Button disabled", disabled=True)

    # st.write("You've clicked", st.session_state.count, "times")

# Case 2:
def handle_click():
    if st.session_state.count < 3:
        st.session_state.count += 1
    if st.session_state.count == 3:
        st.session_state.disable_button = True

if 'count' not in st.session_state:
    st.session_state.count = 0
if 'disable_button' not in st.session_state:
    st.session_state.disable_button = False

st.write("累計次數：", st.session_state.count, "次")

button = st.button("按不過三", disabled=st.session_state.disable_button, on_click=lambda: handle_click())

if st.session_state.count == 3:
    st.write("別再按了")

st.divider()

#-------------------------------------------------------------------
# 下載按鈕
# st.download_button(label, data, file_name=None, mime=None, key=None, help=None, on_click=None, args=None, kwargs=None, *, disabled=False, use_container_width=False)
# MIME 類型：https://www.runoob.com/http/mime-types.html
# -> (bool)

# 下載 CSV
@st.cache_data
def convert_df(df):
    # 取快取，以防每次刷新皆重新生成
    return df.to_csv(index=False).encode('utf-8')

test_csv = convert_df(
    pd.DataFrame(
        np.random.randn(5, 3),
        columns=['A', 'B', 'C']
    )
)

st.download_button(label='Download CSV', data=test_csv, file_name='test.csv', mime='text/csv', key=None)

# 下載文本
text_contents = '''This is some text'''
st.download_button('下載文本', text_contents)

# 下載二進位檔
binary_contents = b'example content'
# Defaults to 'application/octet-stream'
st.download_button('下載二進位檔', binary_contents)

# 下載媒體
with open("./static/image/streamlit-mark-color.png", "rb") as file:
    btn = st.download_button(
            label="下載媒體",
            data=file,
            file_name="flower.png",
            mime="image/png"
        )

st.divider()

#-------------------------------------------------------------------
# 核取方塊
# st.checkbox(label, value=False, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")
# -> (bool)

agree = st.checkbox('I agree')

if agree:
    st.write('Great!')

st.divider()

#-------------------------------------------------------------------
# 選項按鈕
# st.radio(label, options, index=0, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, horizontal=False, label_visibility="visible")
# -> (any)

# Widgets can customize how to hide their labels with the label_visibility parameter.
# If "hidden", the label doesn’t show but there is still empty space for it above the widget (equivalent to label="").
# If "collapsed", both the label and the space are removed. Default is "visible".
# Radio buttons can also be disabled with the disabled parameter, and oriented horizontally with the horizontal parameter:

# Store the initial value of widgets in session state
# 儲存元件 初始值 到 Session State
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False
    st.session_state.horizontal = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable radio widget", key="disabled") # 此時若按下 Check Box
                                                        # Session State 中的 Key 值 {"disabled": False -> True }
                                                        # 下面兩種延伸應用，也是同一概念
    st.checkbox("Orient radio options horizontally", key="horizontal")

with col2:
    st.radio(
        "Set label visibility 👇",
        ["visible", "hidden", "collapsed"],
        key="visibility",
        label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        horizontal=st.session_state.horizontal,
    )

st.divider()

#-------------------------------------------------------------------
# 選單
# st.selectbox(label, options, index=0, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")
# -> (any)

# Store the initial value of widgets in session state
# 同 Radio範例概念，Session State 應用範例：
if "visibility_sb" not in st.session_state:
    st.session_state.visibility_sb = "visible"
    st.session_state.disabled_sb = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable selectbox widget", key="disabled_sb")
    st.radio(
        "Set selectbox label visibility 👉",
        key="visibility_sb",
        options=["visible", "hidden", "collapsed"],
    )

with col2:
    option = st.selectbox(
        "How would you like to be contacted?",
        ("Email", "Home phone", "Mobile phone"),
        label_visibility=st.session_state.visibility_sb,
        disabled=st.session_state.disabled_sb,
    )

st.divider()

#-------------------------------------------------------------------
# 複選欄
# st.multiselect(label, options, default=None, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible", max_selections=None)
# -> (list)

options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])

st.write('You selected:', options)

st.divider()

#-------------------------------------------------------------------
# 滑桿
# st.slider(label, min_value=None, max_value=None, value=None, step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")
# -> (int/float/date/time/datetime or tuple of int/float/date/time/datetime)

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

# Doble-Ended Slider
values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0),
)
st.write("Values:", values)

# period
appointment = st.slider(
    "Schedule your appointment:",
    value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)


start_time = st.slider(
    "When do you start?",
    value=datetime(2020, 1, 1, 9, 30),
    format="YY-MM-DD hh:mm")
st.write("Start time:", start_time)


st.divider()

#-------------------------------------------------------------------
# 選擇滑桿
# st.select_slider(label, options=(), value=None, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")
# -> (any value or tuple of any value)

color = st.select_slider(
    'Select a color of the rainbow',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
st.write(f'My favorite color is {color}')

# Doble-Ended Select Slider
start_color, end_color = st.select_slider(
    'Select a range of color wavelength',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
    value=('red', 'blue'))
st.write('You selected wavelengths between', start_color, 'and', end_color)

st.divider()

#-------------------------------------------------------------------
# 輸入框
# st.text_input(label, value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, *, placeholder=None, disabled=False, label_visibility="visible")
# -> (str)

# Store the initial value of widgets in session state
if "visibility_input" not in st.session_state:
    st.session_state.visibility_input = "visible"
    st.session_state.disabled_input = False

col1, col2 = st.columns(2)

with col1:
    st.checkbox("Disable text input widget", key="disabled_input")
    st.radio(
        "Set text input label visibility 👉",
        key="visibility_input",
        options=["visible", "hidden", "collapsed"],
    )
    st.text_input(
        "Placeholder for the other text input widget",
        "This is a placeholder",
        key="placeholder",
    )

with col2:
    text_input = st.text_input(
        "Enter some text 👇",
        label_visibility=st.session_state.visibility_input,
        disabled=st.session_state.disabled_input,
        placeholder=st.session_state.placeholder,
    )

    if text_input:
        st.write("You entered: ", text_input)

st.divider()

#-------------------------------------------------------------------
# 數字輸入框
# st.number_input(label, min_value=None, max_value=None, value=, step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")
# -> (int, float)

number = st.number_input('Insert a number')
st.write('The current number is ', number)

st.divider()

#-------------------------------------------------------------------
# Text Area
# st.text_area(label, value="", height=None, max_chars=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, placeholder=None, disabled=False, label_visibility="visible")
# -> (str)

txt = st.text_area('Text to analyze', '''
    It was the best of times, it was the worst of times, it was
    the age of wisdom, it was the age of foolishness, it was
    the epoch of belief, it was the epoch of incredulity, it
    was the season of Light, it was the season of Darkness, it
    was the spring of hope, it was the winter of despair, (...)
    ''')
st.write('Sentiment:\n', txt)

st.divider()

#----------------------------------------------
# 日期選擇器
# st.date_input(label, value=None, min_value=None, max_value=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")
# -> (datetime.date or a tuple with 0-2 dates)

d = st.date_input(
    "When\'s your birthday",
    date(2019, 7, 6))
st.write('Your birthday is:', d)

st.divider()

#----------------------------------------------
# 時間選擇器
# st.time_input(label, value=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible", step=0:15:00)
# -> (datetime.time)

t = st.time_input('Set an alarm for', time(8, 45))
st.write('Alarm is set for', t)

st.divider()

#-------------------------------------------------------------------
# 上傳檔案
# st.file_uploader(label, type=None, accept_multiple_files=False, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")
# -> (None or UploadedFile or list of UploadedFile)

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)

# 複數檔案
uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)


st.divider()

#----------------------------------------------
# 視訊截圖
# st.camera_input(label, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")
# -> (None or UploadedFile)

# picture = st.camera_input("Take a picture")

# if picture:
#     st.image(picture)

# #
# img_file_buffer = st.camera_input("Take a picture2")

# if img_file_buffer is not None:
#     # To read image file buffer as bytes:
#     bytes_data = img_file_buffer.getvalue()
#     # Check the type of bytes_data:
#     # Should output: <class 'bytes'>
#     st.write(type(bytes_data))


st.divider()

#----------------------------------------------
# 顏色選擇器
# st.color_picker(label, value=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")
# -> (str)

color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)

st.divider()