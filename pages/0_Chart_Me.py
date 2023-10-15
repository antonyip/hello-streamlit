import time

import altair as alt

import numpy as np
from pandas import *
import streamlit as st
from streamlit.hello.utils import show_code

def chart_me():
    Index= ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
    Cols = ['A', 'B', 'C', 'D']
    df = DataFrame(abs(np.random.randn(5, 4)), index=Index, columns=Cols)
    chart = (
            alt.Chart(df)
            .mark_rect()
            .encode(
                x="index:T",
                y="column:N",
                color="asd:N",
            )
        )
    st.altair_chart(chart)


st.set_page_config(page_title="Plotting Demo", page_icon="📈")
st.markdown("# Plotting Demo")
st.sidebar.header("Plotting Demo")
st.write(
    """This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!"""
)

chart_me()