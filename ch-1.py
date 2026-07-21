import streamlit as st

st.title("Hello app")
st.subheader("Brewed with streamlit")
st.text("Welcomt to your first interactive app")
st.write("Choose your favourite variety of movie")

movie = st.selectbox("Select your favourite movie: ", ['Odyssey', 'Radhe', 'Interstellar']) #jo bhi values ham select karenge vo iss movie variable me store ho jayegi 
st.write(f"You chose {movie}. Excellent choice")
st.success('Your movie has been initialized')


