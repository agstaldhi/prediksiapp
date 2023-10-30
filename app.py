import streamlit as st
import pandas as pd
import pickle
import numpy as np
from PIL import Image

model_landrace = pickle.load(open('model_landrace.sav', 'rb'))
model_yorkshire = pickle.load(open('model_yorkshire.sav', 'rb'))

st.title('Prediksi Angka Kelahiran Hewan Ternak Babi')
image = Image.open('img/pic.png')
st.image(image, width=300)

def predict_landrace(usia, bobot, penyakit, induk):
    result = model_landrace.predict([[0, bobot, usia, penyakit, induk]])

    return result

def predict_yorkshire(usia, bobot, penyakit, induk):
    result = model_yorkshire.predict([[0, bobot, usia, penyakit, induk]])

    return result

def main():
    jenis_option = st.selectbox("Pilih jenis babi", ["Landrace", "Yorkshire"])

    usia = st.slider('Usia (Bulan)', 8, 71, 8)
    bobot = st.slider('Bobot (Kg)', 80, 250, 80)
    chk_penyakit = st.selectbox('Penyakit', ('Ya', 'Tidak'))
    if chk_penyakit == 'Ya':
        penyakit = 1
    else:
        penyakit = 0
    induk = st.slider('Jumlah Indukan Yang Akan Melahirkan', 2, 4, 2)

    if st.button("Prediksi"):
        if jenis_option == "Landrace":
            result = predict_landrace(usia, bobot, penyakit, induk)
        elif jenis_option == "Yorkshire":
            result = predict_yorkshire(usia, bobot, penyakit, induk)

        prediksi = str(result).replace('[', '').replace(']', '')
        hasil = np.round(float(prediksi))
        hasil = int(hasil)
        st.write("Hasil prediksi:", hasil)
        st.write("Jadi untuk 2 minggu kedepan induk babi akan melahirkan sebanyak ", hasil, "ekor anak babi")
        st.write("Dan untuk per ekor indukan babi akan melahirkan sebanyak ", int(hasil/induk), "ekor anak babi")

if __name__ == "__main__":
    main()