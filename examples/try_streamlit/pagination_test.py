import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    # From https://www.kaggle.com/claudiodavi/superhero-set/home
    return pd.read_csv("./data/heroes_information.csv")

st.write(
"""
## 📑 Pagination

Too much data to display? Now you can paginate through items (e.g. a table),
storing the current page number in `st.session_state`.
"""
)
st.write("")
if "page" not in st.session_state:
    st.session_state.page = 0

def next_page():
    st.session_state.page += 1

def prev_page():
    st.session_state.page -= 1

col1, col2, col3, _ = st.columns([0.1, 0.17, 0.1, 0.63]) # 0.1 is the width of the button

if st.session_state.page < 4:
    col3.button("＞", on_click=next_page)
else:
    col3.write("")  # this makes the empty column show up on mobile

if st.session_state.page > 0:
    col1.button("＜", on_click=prev_page)
else:
    col1.write("")  # this makes the empty column show up on mobile

col2.write(f"Page {1 + st.session_state.page} of {5}")

start = 10 * st.session_state.page
end = start + 10

st.write("")
st.write(load_data().iloc[start:end])
