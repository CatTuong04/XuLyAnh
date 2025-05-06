import streamlit as st
import numpy as np
from PIL import Image
from pages import chapter3 as c3

def histogram_page():
    st.title("Histogram - Biểu đồ mức xám (từ ảnh tải lên)")

    # Upload ảnh
    uploaded_file = st.file_uploader("Upload ảnh bất kỳ (jpg, png, bmp, tif)", type=["jpg", "jpeg", "png", "bmp", "tif"])

    if uploaded_file is not None:
        # Đọc ảnh, chuyển sang grayscale
        pil_image = Image.open(uploaded_file).convert("L")
        img = np.array(pil_image)

        # Gọi hàm tính histogram
        hist_img = c3.Histogram(img)
        hist_pil = Image.fromarray(hist_img)

        # Hiển thị 2 ảnh cạnh nhau
        col1, col2 = st.columns(2)
        with col1:
            st.image(pil_image, caption="Ảnh gốc (Grayscale)", use_container_width=True)
        with col2:
            st.image(hist_pil, caption="Biểu đồ Histogram", use_container_width=True)
