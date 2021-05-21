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