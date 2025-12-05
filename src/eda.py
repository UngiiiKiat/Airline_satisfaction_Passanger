import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

def run():
# membuat title
  st.title('Airline Passenger Satisfaction Prediction')

  st.markdown('<p style="font-size: 20px; font-weight: bold;">Eksplorasi Data untuk menganalisa Dataset Airline Passenger Satisfaction</p>', unsafe_allow_html=True)

# Tambahkan gambar
  image = Image.open('src/ipi.jpeg')


  st.image(
     image,
     caption='airpline',
     width=700 # Tentukan lebar dalam piksel
)

# add description
  st.write ('Page ini dibuat oleh ranggakiat')

# Load Data
  df = pd.read_csv('airline_prediction.csv')
  # Tampilin Dataframe
  st.dataframe(df)

# 1
  st.write('### Melihat perbandingan jumlah yang Puas vs Tidak Puas')
  fig = plt.figure(figsize=(15,5))
  sns.countplot(x='satisfaction', hue='satisfaction', data=df, palette='viridis', legend=False)
  plt.title('Total Pelanggan: Puas vs Tidak Puas')
  plt.xlabel('Status Kepuasan')
  plt.ylabel('Jumlah Penumpang')
  plt.show()
  st.pyplot(fig)

# 2
  st.write('### Hubungan Tipe Pelanggan dengan Kepuasan')
  fig = plt.figure(figsize=(8, 5))
  sns.countplot(x='Customer Type', hue='satisfaction', data=df, palette='Set2')
  plt.title('Apakah Pelanggan Loyal Lebih Puas?')
  plt.show()
  st.pyplot(fig)

# 3
  st.write('### Kepuasan berdasarkan Kelas Penerbangan')
  fig = plt.figure(figsize=(8, 5))
  sns.countplot(x='Class', hue='satisfaction', data=df, palette='coolwarm')
  plt.title('Kepuasan Berdasarkan Kelas Penerbangan')
  plt.show()
  st.pyplot(fig)

# 4
  st.write('### Distribusi Umur berdasarkan Kepuasan')
  fig = plt.figure(figsize=(10, 6))
  sns.histplot(data=df, x='Age', hue='satisfaction', kde=True, element="step")
  plt.title('Apakah Faktor Umur Mempengaruhi Kepuasan?')
  plt.show()
  st.pyplot(fig)

# 5
  st.write('### Melihat pola kepuasan berdasarkan Jarak Terbang')
  fig = plt.figure(figsize=(10, 6))
  sns.kdeplot(data=df, x='Flight Distance', hue='satisfaction', fill=True)
  plt.title('Pola Kepuasan pada Jarak Penerbangan Berbeda')
  plt.show()
  st.pyplot(fig)

# 6
  st.write('### Hubungan Rating Wifi dengan Kepuasan')
  fig = plt.figure(figsize=(8, 5))
  sns.countplot(x='Inflight wifi service', hue='satisfaction', data=df, palette='mako')
  plt.title('Dampak Kualitas Wifi Terhadap Kepuasan')
  plt.show()
  st.pyplot(fig)

# 7
  st.write('### Hubungan Online Boarding dengan Kepuasan')
  fig = plt.figure(figsize=(8, 5))
  sns.countplot(x='Online boarding', hue='satisfaction', data=df, palette='rocket')
  plt.title('Pentingnya Kemudahan Online Boarding')
  plt.show()
  st.pyplot(fig)

  # membuat histogram berdasarkan data input
  st.write('### Histogram Interaktif Berdasarkan Input User')
  available_columns = ['satisfaction', 'Ease of Online booking', 'Inflight wifi service', 'Age', 
                       'Arrival Delay in Minutes', 'Departure Delay in Minutes', 'Flight Distance',
                       'Food and drink', 'Cleanliness', 'Type of Travel', 'Class', 'Online boarding']
  option = st.selectbox('Pilih kolom:', available_columns)
  fig = px.histogram(df, x=option, title=f'Distribusi Kolom: {option}')
  sns.histplot(df[option], bins = 30, kde = True)
  st.plotly_chart(fig, use_container_width=True)

  # # membuat dengan plotly express
  # st.write('### Plotly plot - ValueEur and Overall')
  # fig = px.scatter(df, x = 'satisfaction', y = 'Cleanliness', hover_data = ['Class', 'Online boarding'])
  # st.plotly_chart(fig)


if __name__ == '__main__':
  run()
