import streamlit as st
import pandas as pd
import numpy as np

##Title of application
st.title("Hello streamlit")

##Display a simple text
st.write("This is a simple text")

##create a dataframe
df=pd.DataFrame({
    "first coloum": [1, 2, 3, 4],
    "second coloum": [10, 20, 30, 40],
})
print(df)

##Display the dataframe
st.write("Here is our first dataframe:")
st.write(df)

##create a line chart

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"],
)
st.line_chart(chart_data)