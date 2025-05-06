import streamlit as st
import numpy as np
from PIL import Image
from pages import chapter3 as c3
import cv2

def his_equal_color_page():
    st.title("Cân bằng Histogram - Histogram Equalization (Ảnh màu)")

    # Upload ảnh
    uploaded_file = st.file_uploader("Upload ảnh màu (jpg, png, bmp, tif)", type=["jpg", "jpeg", "png", "bmp", "tif"])

    if uploaded_file is not None:
        # Đọc ảnh bằng PIL → chuyển sang numpy
        pil_image = Image.open(uploaded_file).convert("RGB")
        img_rgb = np.array(pil_image)

        # OpenCV dùng BGR, chuyển sang BGR để xử lý
        img_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)

        # Cân bằng histogram bằng hàm HisEqualColor
        img_equalized = c3.HisEqualColor(img_bgr)

        # Chuyển kết quả về RGB để hiển thị bằng PIL
        img_equalized_rgb = cv2.cvtColor(img_equalized, cv2.COLOR_BGR2RGB)
        equalized_pil = Image.fromarray(img_equalized_rgb)

        # Hiển thị hai ảnh cạnh nhau
        col1, col2 = st.columns(2)
        with col1:
            st.image(pil_image, caption="Ảnh gốc (RGB)", use_container_width=True)
        with col2:
            st.image(equalized_pil, caption="Ảnh sau khi cân bằng histogram", use_container_width=True)
