import streamlit as st
import requests

def run():
  
  descripcion = ['Sr', 'Donia', 'Capo']
  pron = st.radio("Elija su pronombre", descripcion)

  edad = st.slider("Cuantos años tiene", 18, 101)

  if st.button('Romper los Huevos con Telegram'):
    st.error(pron+', tiene '+str(edad)+' años y anda hueveando en Telegram...')
    url = 'https://ptm-gateway-20maxbqv.ue.gateway.dev/process?key=AIzaSyB1FDU2Xw-XfssqPhAW3EVZ-7ai2sva3C4'
    x = requests.post(url)
  #file = st.file_uploader("Pick a file")
  #date = st.date_input("Pick a date")