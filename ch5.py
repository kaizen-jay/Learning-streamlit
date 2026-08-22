import streamlit as st
import requests

 #pehle title denge, fir user ko bolenge ki amount choose karo then uske liye input box denge and for user ko bolenge ki kis currency me convert karna hai 

st.title("LIVE CURRENCY CONVERTER")
st.number_input("Enter the amount in INR: ", min_vlaue = 1)

target_currency = st.selectbox("Convert to:", ["USD", "EUR", "GBP", "JPY"])

if st.button("Convert"):
    url = "https://api.exchangerate-api.com/v4/latest/inr"
    response = requests.get(url)

    if response.status_code == 200:
        response.json #jo bhi response aaya hai pehle usko json me karte hai taaki ham values use to kar paaye
    else:
        st.error("Failed to fetch conversion rate")

