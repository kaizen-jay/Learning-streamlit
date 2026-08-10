import streamlit as st
from datetime import date

st.title("AGE CALCULATOR USING STREAMLIT")
dob= st.date_input("Enter your Date of Birth: ", min_value=date(1900,1,1), max_value=date.today())
today = date.today()
age = today.year - dob.year

if age >= 18:
    st.success(f"Your age is {age} years. And you are an adult.")
else:
    st.success(f"Your age is {age} years. And you are a minor.")





