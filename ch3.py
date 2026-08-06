import streamlit as st

st.title("Chai Taste Poll ")

col1,col2 = st.columns(2) #two columns whose names are col1 and 2
with col1: #har column bhi apne aap me ek page ki tarah treat hota hai 
    st.header("Masala Chai")
    vote1 = st.button("Vote masala chai")
with col2:
    st.header("Adrak Chai")
    vote2 = st.button("Vote adrak chai") 

if vote1:
    st.success("Thanks for voting masala chai")
elif vote2:
    st.success("Thanks for voting adrak chai")

# making github green.
