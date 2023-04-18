# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import streamlit as st

#======================================================
# 資料顯示物件
#------------------------------------------------
# DataFrame
# 支援型別繁多 (pandas.DataFrame, pandas.Styler, pyarrow.Table, numpy.ndarray, pyspark.sql.DataFrame, snowflake.snowpark.dataframe.DataFrame, snowflake.snowpark.table.Table, Iterable, dict, or None)

df = pd.DataFrame(
    np.random.randn(10 ,20),
    columns = (f'col {i}' for i in range(20))
)

st.header('DataFrame')
st.write('支援 pandas 的 styler')
st.caption('(pandas.DataFrame.style)')

st.write(df.style.highlight_max(axis=0))

st.dataframe(df.style.highlight_min(axis=1))

# 版型調整參數
# 快取避免重複建立 DataFrame
@st.cache_data
def load_data():
    return pd.DataFrame(
        {
            "first column": [1, 2, 3, 4],
            "second column": [10, 20, 30, 40],
        }
    )

# 建立 Check box
st.checkbox("Use container width", value=False, key="use_container_width")

df = load_data()

# 用 Check box 選擇比對，原型 (200px * 100px) & 適應容器寬
st.dataframe(df, 200, 100, use_container_width=st.session_state.use_container_width)


st.divider()

#------------------------------------------------
# 靜態表格
# 支援型別同 st.DataFrame

st.header('靜態表格')

df = pd.DataFrame(
   np.random.randn(10, 5),
   columns=(f'col {i}' for i in range(5))
)

st.table(df)

st.divider()

#------------------------------------------------
# 度量指標
# delta 顏色預設 綠升紅降，可調反轉或關閉(灰)

st.header('度量指標')

st.metric(label="Gas price", value=4, delta=-0.5,
    delta_color="inverse")

st.metric(label="Active developers", value=123, delta=123,
    delta_color="off")

st.divider()

#------------------------------------------------
# 字典 & JSON

st.header('字典 & JSON')

st.json({
    'foo': 'bar',
    'baz': 'boz',
    'stuff': [
        'stuff 1',
        'stuff 2',
        'stuff 3',
        'stuff 5',
    ],
}, expanded=False)
