import streamlit as st
import pandas as pd
st.title("Chai sales dashboard")
file = st.file_uploader("Upload your csv file", type=["csv"])
if file:
    df = pd.read_csv(file)
    st.subheader("Data preview")
    st.dataframe(df) #Pandas ke sath streamlit ka kaafi close relation hai 
if file:
    st.subheader("Summary of the data")
    st.write(df.describe())
# this is somethibn intersting to do with pandas
# If we wanted to pick out all the unique values form a column we can just use the pandas function just like:

if file:
    