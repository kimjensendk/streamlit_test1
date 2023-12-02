import streamlit as st
import pandas as pd
import numpy as np

df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                   columns=['a', 'b', 'c'])



st.title('Hello world dette er headeren på denn streamlit app')

st.header('header')

st.text('txt')

st.dataframe(df2)

st.dataframe(df2.plot())
