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
    genders = df["sex"].unique()
    gender = st.selectbox("Filter by gender", genders) #means select box ko do parameters lagte hai first is filter by gender and parameter diya genderr.

#Ham dataframes ke andar unique values ko select kar sakte hai and aur uska bhi dataframe bana sakte hai  
    filtered_data = df[df["sex"] == gender]   #matlab ki ham sex dataframe ko select karna chahte hai . and agar is sex ki value equal ho gender ke andar to iss poore ko ham dataframe bana denge . Isse hoga ye ki poora filtered data ho jayega (more in pandas section) 
    #Now to display the outcome:
    st.dataframe(filtered_data) #matlab ki mujhe jo dataframe display karna hai vo de denge