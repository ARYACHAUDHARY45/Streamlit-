import streamlit as st
import pandas as pd

st.title("Streamlit Text input")

name=st.text_input("Enter your name")


age=st.slider("Select your age", 0, 100, 25)
st.write(f"You are {age} years old.")

options=["python", "java", "c++", "javascript"]
choice=st.selectbox("Select your favorite programming language", options)
st.write(f"You selected: {choice}")

if name:
    st.write(f"Hello {name}!")

data={
    "Name": [name],
    "Age": [age],
    "Language": [choice]
}
df=pd.DataFrame(data)
df.to_csv("sample.csv", index=False)
st.write(df)

uploaded_file = st.file_uploader("choose a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Data from the uploaded CSV file:")
    st.write(df)


    
