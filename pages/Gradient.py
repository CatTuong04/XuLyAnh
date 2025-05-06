import streamlit as st
import numpy as np
from PIL import Image
from pages import chapter3 as c3  # Hàm Gradient(img) cần trả về ảnh uint8

def gradient_image_page():
    st.title("Phát hiện biên bằng Gradient")

    uploaded_file = st.file_uploader("Upload ảnh bất kỳ (jpg, png, bmp, tif)", type=["jpg", "jpeg", "png", "bmp", "tif"])

    if uploaded_file is not None:
        # Đọc ảnh và chuyển sang grayscale
        pil_image = Image.open(uploaded_file).convert("L")
        img_gray = np.array(pil_image)

        # Áp dụng Gradient
        img_gradient = c3.Gradient(img_gray)
        result_pil = Image.fromarray(img_gradient)

        # Hiển thị ảnh gốc và ảnh gradient cạnh nhau
        col1, col2 = st.columns(2)
        with col1:
            st.image(pil_image, caption="Ảnh gốc (Grayscale)", use_container_width=True)
        with col2:
            st.image(result_pil, caption="Ảnh sau khi áp dụng Gradient", use_container_width=True)
