import streamlit as st
import numpy as np
from PIL import Image
from pages import chapter3 as c3  # đảm bảo đã có hàm MyMedianFilter2()

def median_filter_page():
    st.title("Lọc Median (Lọc trung vị)")

    uploaded_file = st.file_uploader("Upload ảnh bất kỳ (jpg, png, bmp, tif)", type=["jpg", "jpeg", "png", "bmp", "tif"])

    if uploaded_file is not None:
        # Đọc ảnh và chuyển sang grayscale
        pil_image = Image.open(uploaded_file).convert("L")
        img_gray = np.array(pil_image)

        # Áp dụng lọc Median
        img_median = c3.MyMedianFilter2(img_gray)
        result_pil = Image.fromarray(img_median)

        # Hiển thị ảnh gốc và kết quả cạnh nhau
        col1, col2 = st.columns(2)
        with col1:
            st.image(pil_image, caption="Ảnh gốc (Grayscale)", use_container_width=True)
        with col2:
            st.image(result_pil, caption="Ảnh sau khi lọc Median", use_container_width=True)
