import streamlit as st
import numpy as np
from PIL import Image
from pages import chapter3 as c3

def power_image_page():
    st.title("Power Transformation - Biến đổi lũy thừa (từ ảnh tải lên)")

    uploaded_file = st.file_uploader("Upload ảnh bất kỳ (jpg, png, bmp, tif)", type=["jpg", "jpeg", "png", "bmp", "tif"])

    if uploaded_file is not None:
        # Chọn gamma
        gamma = st.slider("Chọn giá trị gamma", min_value=0.1, max_value=10.0, value=5.0, step=0.1)

        # Đọc ảnh và chuyển grayscale
        pil_image = Image.open(uploaded_file).convert("L")
        img = np.array(pil_image)

        # Hiển thị ảnh gốc
        col1, col2 = st.columns(2)
        with col1:
            st.image(pil_image, caption="Ảnh gốc (Grayscale)", use_container_width=True)

        # Gọi hàm Power có thêm gamma
        img_out = c3.Power(img, gamma)  # Cập nhật hàm Power để nhận gamma làm tham số
        result_pil = Image.fromarray(img_out)

        with col2:
            st.image(result_pil, caption=f"Ảnh sau biến đổi lũy thừa (γ = {gamma})", use_container_width=True)
