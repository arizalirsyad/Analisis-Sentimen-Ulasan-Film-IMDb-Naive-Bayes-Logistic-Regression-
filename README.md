# 🎬 Analisis Sentimen Ulasan Film IMDb

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://arizalirsyad-analisis-sentimen-ulasan-film-imdb-naiv-app-lpfc9h.streamlit.app/)
[![3.10.0](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)

Proyek ini adalah aplikasi web interaktif berbasis **Streamlit** untuk melakukan klasifikasi sentimen pada ulasan film (IMDb). Model *Machine Learning* yang digunakan dapat memprediksi apakah sebuah teks ulasan memiliki sentimen **Positif** atau **Negatif**.

## Live Demo
Aplikasi ini telah di-deploy dan dapat diakses secara langsung melalui tautan berikut:
**[Buka Aplikasi Analisis Sentimen IMDb](https://arizalirsyad-analisis-sentimen-ulasan-film-imdb-naiv-app-lpfc9h.streamlit.app/)**

---

## 🧠 Algoritma Machine Learning
Proyek ini membandingkan dan mengimplementasikan dua algoritma klasifikasi teks tradisional yang efisien:
*   **Naive Bayes:** Cepat dan efektif untuk klasifikasi teks dengan asumsi independensi antar fitur.
*   **Logistic Regression:** Menawarkan probabilitas yang dapat diinterpretasikan dan performa yang sangat baik untuk dataset teks besar.

Proses ekstraksi fitur teks dilakukan menggunakan **TF-IDF Vectorizer** (*Term Frequency-Inverse Document Frequency*).

## 🛠️ Teknologi yang Digunakan
*   **Python 3.x**
*   **Streamlit:** Pembuatan antarmuka web (UI) interaktif.
*   **Scikit-Learn:** Pelatihan model, evaluasi metrik, dan pemrosesan TF-IDF.
*   **Joblib:** Penyimpanan dan pemuatan model yang telah dilatih (*model persistence*).
*   **Pandas & NumPy:** Manipulasi dan analisis data.

---

## 📂 Struktur Direktori Proyek

```text
├── models/                  # Folder untuk menyimpan file .pkl (model & vectorizer)
├── notebooks/               # File Jupyter Notebook (EDA, preprocessing, dan training)
├── app.py                   # Script utama aplikasi Streamlit
├── requirements.txt         # Daftar library Python yang dibutuhkan
└── README.md                # Dokumentasi proyek ini
