import streamlit as st
import numpy as np
from PIL import Image
from pages import chapter3 as c3

def hist_stat_page():
    st.title("Thống kê Histogram (Histogram Statistics)")

    uploaded_file = st.file_uploader("Upload ảnh bất kỳ (jpg, png, bmp, tif)", type=["jpg", "jpeg", "png", "bmp", "tif"])

    if uploaded_file is not None:
        # Chuyển ảnh sang grayscale
        pil_image = Image.open(uploaded_file).convert("L")
        img_gray = np.array(pil_image)

        # Áp dụng xử lý Histogram Statistics
        img_hist_stat = c3.HistStat(img_gray)
        result_pil = Image.fromarray(img_hist_stat)

        # Hiển thị hai ảnh cạnh nhau
        col1, col2 = st.columns(2)
        with col1:
            st.image(pil_image, caption="Ảnh gốc (Grayscale)", use_container_width=True)
        with col2:
            st.image(result_pil, caption="Ảnh sau xử lý Histogram Statistics", use_container_width=True)
