import streamlit as st
import numpy as np
from PIL import Image
from pages import chapter3 as c3

def smooth_box_page():
    st.title("Lọc ảnh bằng Box Filter (Lọc trung bình)")

    uploaded_file = st.file_uploader("Upload ảnh bất kỳ (jpg, png, bmp, tif)", type=["jpg", "jpeg", "png", "bmp", "tif"])

    if uploaded_file is not None:
        # Đọc và chuyển ảnh sang grayscale
        pil_image = Image.open(uploaded_file).convert("L")
        img_gray = np.array(pil_image)

        # Áp dụng lọc trung bình Box
        img_box = c3.MySmoothBox(img_gray)
        result_pil = Image.fromarray(img_box)

        # Hiển thị ảnh gốc và ảnh đã lọc bên cạnh nhau
        col1, col2 = st.columns(2)
        with col1:
            st.image(pil_image, caption="Ảnh gốc (Grayscale)", use_column_width=True)
        with col2:
            st.image(result_pil, caption="Ảnh sau khi lọc Box", use_column_width=True)
