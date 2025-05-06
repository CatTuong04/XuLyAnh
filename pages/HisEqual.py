import streamlit as st
import numpy as np
from PIL import Image
from pages import chapter3 as c3

def his_equal_page():
    st.title("Cân bằng Histogram - Histogram Equalization (Grayscale)")

    # Upload ảnh
    uploaded_file = st.file_uploader("Upload ảnh bất kỳ (jpg, png, bmp, tif)", type=["jpg", "jpeg", "png", "bmp", "tif"])

    if uploaded_file is not None:
        # Đọc ảnh, chuyển sang grayscale
        pil_image = Image.open(uploaded_file).convert("L")
        img = np.array(pil_image)

        # Gọi hàm cân bằng histogram
        equalized_img = c3.HisEqual(img)
        equalized_pil = Image.fromarray(equalized_img)

        # Hiển thị hai ảnh cạnh nhau
        col1, col2 = st.columns(2)
        with col1:
            st.image(pil_image, caption="Ảnh gốc (Grayscale)", use_container_width=True)
        with col2:
            st.image(equalized_pil, caption="Ảnh sau khi cân bằng histogram", use_container_width=True)
