import streamlit as st 
import eda
import prediction

page = st.sidebar.selectbox('Pilih halaman: ', ('EDA', 'Prediction'))

if page == 'EDA':
  eda.run()
else:
  prediction.run()