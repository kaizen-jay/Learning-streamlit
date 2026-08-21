import streamlit as st
import pandas as pd
st.title("Chai sales dashboard")
file = st.file_uploader("Upload your csv file", type=["csv"])
if file:
    df = pd.read_csv(file)
    st.subheader("Data preview")
    st.dataframe(df) #Pandas ke sath streamlit ka kaafi close relation hai 
if file:
    st.subheader("Summary stats")
    st.write(df.describe())
# this is somethibn intersting to do with pandas
# If we wanted to pick out all the unique values form a column we can just use the pandas function just like:

if file:
    cities = df["City"].unique() # hamne genders variable ke andar ek 'sex' naam ka column le liya hai jiski saari unique values ham isme store kar rahe hai.   
    selected_city = st.selectbox("Filter by cities", cities) #means select box ko do parameters lagte hai first is filter by gender and parameter diya genderr.

#Ham dataframes ke andar unique values ko select kar sakte hai and aur uska bhi dataframe bana sakte hai  
    filtered_data = df[df["City"] == selected_city] #matlab ki ham sex dataframe ko select karna chahte hai . and agar is sex ki value equal ho gender ke andar to iss poore ko ham dataframe bana denge . Isse hoga ye ki poora filtered data ho jayega (more in pandas section) 
    #Now to display the outcome:
    st.dataframe(filtered_data) #matlab ki mujhe jo dataframe display karna hai vo de denge

    # isse hota ye hai ki jo value hamne li hai waha waha true ho gayaai and alag column ban gaya hai jaha pe jo true values hai bas vo display hongi...