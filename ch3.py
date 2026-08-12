import streamlit as st

st.title("Chai Taste Poll ")

col1,col2 = st.columns(2) #two columns whose names are col1 and 2
with col1: #har column bhi apne aap me ek page ki tarah treat hota hai 
    st.header("Masala Chai")
    st.image("https://imgs.search.brave.com/jGNfavdSOBAxPsdDw6bxW29oO5BpyjXRdWYg0HR78yg/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly93d3cu/cGFyc2lkYWlyeWZh/cm0uY29tL2Nkbi9z/aG9wL2ZpbGVzLzNf/Q2hhaU1hc2FsYV8z/NzV4Mzc1X2Nyb3Bf/Y2VudGVyLmpwZz92/PTE3MDkwMTIzNjg" , width = 200)
    vote1 = st.button("Vote masala chai")
with col2:
    st.header("Adrak Chai")
    st.image("https://imgs.search.brave.com/KQ4xKWpIJmPeEga9pCXqRPSoKGwwMgnfbD5zh5r1gs0/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9oZWJi/YXJza2l0Y2hlbi5j/b20vd3AtY29udGVu/dC91cGxvYWRzLzIw/MTkvMDgvZ2luZ2Vy/LXRlYS1yZWNpcGUt/YWRyYWstY2hhaS1h/ZHJhay13YWxpLWNo/YWktZ2luZ2VyLW1p/bGstdGVhLTItMTAy/NHg2ODIuanBlZw" , width = 200)
    vote2 = st.button("Vote adrak chai") 

if vote1:
    st.success("Thanks for voting masala chai")
elif vote2:
    st.success("Thanks for voting adrak chai")

# making github green..
