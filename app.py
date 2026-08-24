import streamlit as st
import joblib

# 1. Muat model dan vectorizer (yang sudah disimpan sebelumnya)
model = joblib.load('models/logistic_regression_model.pkl')
vectorizer = joblib.load('models/tfidf_vectorizer.pkl')

# 2. Buat Antarmuka Web
st.title("🎬 Analisis Sentimen Ulasan Film")
ulasan = st.text_area("Masukkan teks ulasan dalam bahasa Inggris:")

if st.button("Analisis Sentimen"):
    # 3. Proses input dan tampilkan hasil
    vektor_teks = vectorizer.transform([ulasan])
    prediksi = model.predict(vektor_teks)
    
    if prediksi[0] == 1:
        st.success("Sentimen: POSITIF ")
    else:
        st.error("Sentimen: NEGATIF ")