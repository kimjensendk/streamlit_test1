import streamlit as st
import pandas as pd
import numpy as np

df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                   columns=['a', 'b', 'c'])



st.title('Hello world dette er headeren på denn streamlit app')

st.header('header')

st.text('txt')

st.dataframe(df2)

df = pd.DataFrame({'length': [1.5, 0.5, 1.2, 0.9, 3],
                  'width': [0.7, 0.2, 0.15, 0.2, 1.1]},
                  index=['pig', 'rabbit', 'duck', 'chicken', 'horse'])
st.dataframe(df.plot(title="DataFrame Plot"))

