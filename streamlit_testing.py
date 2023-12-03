import streamlit as st
import pandas as pd
import numpy as np


df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                   columns=['a', 'b', 'c'])



st.title('Hello world')

st.header('Nu skal der ')

st.text('Her står der noget standard tekst alm størrelse')

df = pd.DataFrame(np.random.randn(10, 20), columns=("col %d" % i for i in range(20)))

st.dataframe(df.style.highlight_max(axis=0))

