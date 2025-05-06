import streamlit as st
import numpy as np
import cv2
from PIL import Image

def spectrum_page():
    st.title("Biến đổi Fourier - Hiển thị Spectrum")

    uploaded_file = st.file_uploader("Upload ảnh (jpg, png, bmp, tif)", type=["jpg", "jpeg", "png", "bmp", "tif"])

    if uploaded_file is not None:
        # Đọc ảnh và chuyển sang grayscale
        img_pil = Image.open(uploaded_file).convert("L")
        img_gray = np.array(img_pil)

        # Biến đổi Fourier
        f = np.fft.fft2(img_gray)
        fshift = np.fft.fftshift(f)
        magnitude_spectrum = 20 * np.log(np.abs(fshift) + 1)

        # Chuẩn hóa và ép kiểu để hiển thị
        mag_norm = cv2.normalize(magnitude_spectrum, None, 0, 255, cv2.NORM_MINMAX)
        mag_uint8 = np.uint8(np.clip(mag_norm, 0, 255))
        spectrum_pil = Image.fromarray(mag_uint8)

        # Hiển thị ảnh gốc và phổ bên cạnh nhau
        col1, col2 = st.columns(2)
        with col1:
            st.image(img_pil, caption="Ảnh gốc (Grayscale)", use_container_width=True)
        with col2:
            st.image(spectrum_pil, caption="Magnitude Spectrum", use_container_width=True)
