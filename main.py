import streamlit as st

st.title("Hello app")
st.subheader("Brewed with streamlit")
st.text("Welcomt to your first interactive app")
st.write("Choose your favourite variety of movie")

movie = st.selectbox()
