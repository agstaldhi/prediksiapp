import streamlit as st
import pandas as pd
import pickle
from PIL import Image
import numpy as np

model_landrace = pickle.load(open('model_landrace.sav', 'rb'))
model_yorkshire = pickle.load(open('model_yorkshire.sav', 'rb'))

st.title('Prediksi Angka Kelahiran Hewan Ternak Babi')
image = Image.open('img/pic.png')
st.image(image, width=300)

def predict_landrace(usia, bobot, penyakit):
    result = model_landrace.predict([[0, bobot, usia, penyakit]])

    return result

def predict_yorkshire(usia, bobot, penyakit):
    result = model_yorkshire.predict([[0, bobot, usia, penyakit]])

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

    if st.button("Prediksi"):
        if jenis_option == "Landrace":
            result = predict_landrace(usia, bobot, penyakit)
        elif jenis_option == "Yorkshire":
            result = predict_yorkshire(usia, bobot, penyakit)

        prediksi = str(result).replace('[','').replace(']','')
        hasil = np.round(float(prediksi))
        hasil = int(hasil)
        st.write("Hasil Prediksi:", hasil)
        st.write("Jadi untuk 2 minggu kedepan Babi akan melahirkan sebanyak:", hasil,"Ekor anak babi")

if __name__ == "__main__":
    main()