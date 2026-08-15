import streamlit as st
import pandas as pd
st.title("Chai sales dashboard")
file = st.file_uploader("Upload your csv file", type=["csv"])
if file:
    df = pd.read_csv(file)
    st.subheader("Data preview")
    st.dataframe(df) #Pandas ke sath streamlit ka kaafi close relation hai 
