import streamlit as st
import numpy as np
from PIL import Image
from pages import chapter3 as c3

def piecewise_linear_page():
    st.title("Piecewise Linear Transformation - Biến đổi tuyến tính (từ ảnh tải lên)")

    # Tải ảnh
    uploaded_file = st.file_uploader("Upload ảnh bất kỳ (jpg, png, bmp, tif)", type=["jpg", "jpeg", "png", "bmp", "tif"])

    if uploaded_file is not None:
        # Đọc ảnh bằng PIL và chuyển sang numpy (grayscale)
        pil_image = Image.open(uploaded_file).convert("L")
        img = np.array(pil_image)

        # Gọi hàm xử lý từ chapter3
        img_out = c3.PiecewiseLine(img)
        result_pil = Image.fromarray(img_out)

        # Hiển thị ảnh gốc và kết quả cạnh nhau
        col1, col2 = st.columns(2)
        with col1:
            st.image(pil_image, caption="Ảnh gốc (Grayscale)", use_container_width=True)
        with col2:
            st.image(result_pil, caption="Ảnh sau biến đổi tuyến tính", use_container_width=True)
