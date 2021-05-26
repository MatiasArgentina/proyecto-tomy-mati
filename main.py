import streamlit as st
import numpy as np
import pandas as pd
import process

USER_PASSWORD = "furgoneta"

password = st.text_input("Enter a password", type="password")

if password:
  if password != USER_PASSWORD:
    st.error("the password you entered is incorrect")
  else:
    process.run()

number = st.slider("Pick a number", 0, 100)

file = st.file_uploader("Pick a file")

pets = ['dog', 'cat', 'fish']
pet = st.radio("Pick a pet", pets)

date = st.date_input("Pick a date")