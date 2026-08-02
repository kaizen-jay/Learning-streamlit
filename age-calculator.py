import streamlit as st
from datetime import date 
st.title("AGE CALCULATOR USING STREAMLIT")

dob = st.date_input("Enter your date of birth: ", value= date.today(), min_value=date(1900,1,1), max_value=date(3600,1,1))

st.write(f"The entered date of birth is {dob} .")





