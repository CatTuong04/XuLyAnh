import streamlit as st
import numpy as np
from PIL import Image
from pages import chapter3 as c3  # Đảm bảo có hàm Sharp()

def sharpen_image_page():
    st.title("Làm sắc nét ảnh (Sharpen)")

    uploaded_file = st.file_uploader("Upload ảnh bất kỳ (jpg, png, bmp, tif)", type=["jpg", "jpeg", "png", "bmp", "tif"])

    if uploaded_file is not None:
        # Đọc và chuyển ảnh sang grayscale
        pil_image = Image.open(uploaded_file).convert("L")
        img_gray = np.array(pil_image)

        # Làm sắc nét
        img_sharp = c3.Sharp(img_gray)
        result_pil = Image.fromarray(img_sharp)

        # Hiển thị song song ảnh gốc và ảnh sắc nét
        col1, col2 = st.columns(2)
        with col1:
            st.image(pil_image, caption="Ảnh gốc (Grayscale)", use_container_width=True)
        with col2:
            st.image(result_pil, caption="Ảnh sau khi làm sắc nét", use_container_width=True)
