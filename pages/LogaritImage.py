import streamlit as st
import cv2
import numpy as np
from PIL import Image
from pages import chapter3 as c3

def logarithmic_image_page():
    st.title("Logarithmic Image - Biến đổi Log (từ ảnh tải lên)")

    # Tải ảnh lên
    uploaded_file = st.file_uploader("Upload ảnh bất kỳ (jpg, png, bmp, tif)", type=["jpg", "jpeg", "png", "bmp", "tif"])

    if uploaded_file is not None:
        # Đọc ảnh và chuyển sang grayscale
        pil_image = Image.open(uploaded_file).convert("L")
        img = np.array(pil_image)

        # Xử lý ảnh log ngay sau khi upload
        img_out = c3.Logarit(img)
        result_pil = Image.fromarray(img_out)

        # Hiển thị ảnh cạnh nhau
        col1, col2 = st.columns(2)
        with col1:
            st.image(pil_image, caption="Ảnh gốc (Grayscale)", use_container_width=True)
        with col2:
            st.image(result_pil, caption="Ảnh Logarithmic", use_container_width=True)
