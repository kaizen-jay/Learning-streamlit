'''Making widgets in streamlit'''

import streamlit as st
 
st.title('Chai maker app')
if st.button ('Make chai'):
    st.success('Your chai is being brewed')
add_masala = st.checkbox('Add masala to the chai') #We can make to do apps from this bcz its a checklist
if add_masala:
    st.write('Masala added to chai')

tea_type = st.radio('Pick your chai base: ', ['Milk', 'Water', 'Honey'])
st.write(f'Selected base is {tea_type}')
flavour = st.selectbox('Choose Flavour', ['Adrak', 'Kesar', 'Tulsi'])
st.write(f'Selected flavour is {flavour}')

sugar = st.slider("Sugar Spoons", 0, 5, 2) #here 2 is the default value 

st.write(f"Selected sugar spoons is {sugar}")

name = st.text_input("Enter your name: ")
if name: #this indicates if any value is entered in name it will perfor something inside the if statement
    st.write(f"Welcome, {name} ! Your chai is ready")






