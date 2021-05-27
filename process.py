import streamlit as st

def run():
  number = st.slider("Pick a number", 0, 100)

  file = st.file_uploader("Pick a file")

  pets = ['dog', 'cat', 'fish']
  pet = st.radio("Pick a pet", pets)

  date = st.date_input("Pick a date")