import streamlit as st
import numpy as np
from PIL import Image
from pages import chapter3 as c3  # đảm bảo đã có hàm Hubble()

def threshold_page():
    st.title("Phân ngưỡng ảnh (Thresholding)")

    uploaded_file = st.file_uploader("Upload ảnh bất kỳ (jpg, png, bmp, tif)", type=["jpg", "jpeg", "png", "bmp", "tif"])

    if uploaded_file is not None:
        # Đọc và chuyển ảnh sang grayscale
        pil_image = Image.open(uploaded_file).convert("L")
        img_gray = np.array(pil_image)

        # Áp dụng phân ngưỡng (dùng hàm Hubble)
        img_thresh = c3.Hubble(img_gray)
        result_pil = Image.fromarray(img_thresh)

        # Hiển thị hai ảnh cạnh nhau
        col1, col2 = st.columns(2)
        with col1:
            st.image(pil_image, caption="Ảnh gốc (Grayscale)", use_container_width=True)
        with col2:
            st.image(result_pil, caption="Ảnh sau khi phân ngưỡng", use_container_width=True)
