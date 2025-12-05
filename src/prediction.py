import streamlit as st
import joblib
import pandas as pd
import numpy as np


@st.cache_resource
def load_pipeline():
    try:
        model = joblib.load('final_rf_satisfaction_model.joblib')
        return model
    except FileNotFoundError:
        st.error("file hilang")
        return None

model_pipeline = load_pipeline()


def run():
  st.title("✈️ Prediksi Kepuasan Pelanggan Maskapai")
  st.markdown("Masukkan detail pengalaman penerbangan untuk memprediksi kepuasan penumpang.")

  if model_pipeline is not None:
      st.header("Faktor Kritis & Perjalanan")
      col1, col2 = st.columns(2)
      with col1:
          flight_distance = st.number_input("Jarak Penerbangan (mil)", min_value=100, max_value=10000, value=1500)
          customer_type = st.selectbox("Tipe Pelanggan", ['Loyal Customer', 'disloyal Customer'])
          travel_type = st.selectbox("Tipe Perjalanan", ['Business travel', 'Personal Travel'])
      with col2:
          age = st.number_input("Umur Penumpang", min_value=1, max_value=90, value=30)
          flight_class = st.selectbox("Kelas Penerbangan", ['Business', 'Eco', 'Eco Plus'])
          arrival_delay = st.number_input("Keterlambatan Kedatangan (menit)", min_value=0, max_value=30, value=5)


# Kolom Rating Layanan (Ordinal: 1-5)
      st.header("Rating Layanan (Skala 1 - 5)")
      st.markdown("5 = Sangat Baik, 1 = Sangat Buruk")
    
# menggunakan rating 1-5 (atau 0-5)
      col_rating_1, col_rating_2, col_rating_3 = st.columns(3)

# Kolom Rating Paling Penting (Sesuai F-Score Tinggi)
      with col_rating_1:
          st.subheader("Teknologi")
          wifi = st.slider("Layanan Wifi Pesawat", 1, 5, 4)
          online_boarding = st.slider("Kemudahan Online Boarding", 1, 5, 5)
          ease_online_booking = st.slider("Kemudahan Booking Online", 1, 5, 4)

# Kolom Rating Kenyamanan
      with col_rating_2:
          st.subheader("Kenyamanan")
          seat_comfort = st.slider("Kenyamanan Kursi", 1, 5, 4)
          leg_room = st.slider("Ruang Kaki (Leg Room)", 1, 5, 4)
          cleanliness = st.slider("Kebersihan Pesawat", 1, 5, 5)

# Kolom Rating Service
      with col_rating_3:
          st.subheader("Pelayanan")
          food_drink = st.slider("Makanan & Minuman", 1, 5, 3)
          checkin_service = st.slider("Layanan Check-in", 1, 5, 4)
          inflight_service = st.slider("Layanan Dalam Penerbangan", 1, 5, 4)
        
        # Sisa Kolom yang Anda gunakan (Asumsi rating 1-5)
          inflight_entertainment = st.slider("Hiburan", 1, 5, 4)
          onboard_service = st.slider("Layanan Kru", 1, 5, 4)
          baggage_handling = st.slider("Penanganan Bagasi", 1, 5, 4)

      if st.button("Prediksi Kepuasan"):
          input_data = pd.DataFrame({
              'Flight_Distance': [flight_distance],
              'Age': [age],
              'Arrival_Delay_in_Minutes': [arrival_delay],
              'Inflight_wifi_service': [wifi],
              'Ease_of_Online_booking': [ease_online_booking],
              'Food_and_drink': [food_drink],
              'Online_boarding': [online_boarding],
              'Seat_comfort': [seat_comfort],
              'Inflight_entertainment': [inflight_entertainment],
              'On-board_service': [onboard_service],
              'Leg_room_service': [leg_room],
              'Baggage_handling': [baggage_handling],
              'Checkin_service': [checkin_service],
              'Inflight_service': [inflight_service],
              'Cleanliness': [cleanliness],
            # Kolom Kategorikal
              'Customer_Type': [customer_type],
              'Type_of_Travel': [travel_type],
              'Class': [flight_class]
          })
        
        # Lakukan prediksi (Model Pipeline akan otomatis Scaling & Encoding)
          prediction = model_pipeline.predict(input_data)
          prediction_proba = model_pipeline.predict_proba(input_data)
        
        # Ambil hasil
          status = 'Puas (SATISFIED)' if prediction[0] == 1 else 'Tidak Puas (DISSATISFIED)'
          prob_satisfied = prediction_proba[0][1] * 100
        
        # tampilan hasil
          st.subheader("Hasil Prediksi")
        
          if status == 'Puas (SATISFIED)':
              st.success(f"Penumpang diprediksi: {status}")
              st.markdown(f"**Probabilitas Puas:** **{prob_satisfied:.2f}%**")
          else:
              st.warning(f"Penumpang diprediksi: {status} (Risiko Churn)")
              st.markdown(f"**Probabilitas Tidak Puas:** **{100 - prob_satisfied:.2f}%**")
              st.info("Rekomendasi Bisnis: Segera lakukan intervensi atau tawarkan kompensasi kecil.")

if __name__ == '__main__':
  run()