import streamlit as st
import numpy as np
from PIL import Image
from pages import chapter3 as c3

def local_hist_page():
    st.title("Cân bằng Histogram cục bộ - Local Histogram Equalization")

    # Upload ảnh
    uploaded_file = st.file_uploader("Upload ảnh bất kỳ (jpg, png, bmp, tif)", type=["jpg", "jpeg", "png", "bmp", "tif"])

    if uploaded_file is not None:
        # Đọc ảnh và chuyển về grayscale
        pil_image = Image.open(uploaded_file).convert("L")
        img_gray = np.array(pil_image)

        # Xử lý bằng Local Histogram
        img_local = c3.LocalHist(img_gray)
        local_pil = Image.fromarray(img_local)

        # Hiển thị ảnh gốc và ảnh sau xử lý cạnh nhau
        col1, col2 = st.columns(2)
        with col1:
            st.image(pil_image, caption="Ảnh gốc (Grayscale)", use_container_width=True)
        with col2:
            st.image(local_pil, caption="Ảnh sau Local Histogram Equalization", use_container_width=True)
