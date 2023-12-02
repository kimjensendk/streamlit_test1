import streamlit as st
import pandas as pd
import numpy as np

df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                   columns=['a', 'b', 'c'])



st.title('Hello world dette er headeren på denn streamlit app')

st.header('header')

st.text('txt')

st.dataframe(df2)

speed = [0.1, 17.5, 40, 48, 52, 69, 88]
lifespan = [2, 8, 70, 1.5, 25, 12, 28]
index = ["snail", "pig", "elephant", "rabbit", "giraffe", "coyote", "horse"]
df = pd.DataFrame({"speed": speed, "lifespan": lifespan}, index=index)

st.pyplot(df.plot.barh(stacked=True).figure)

