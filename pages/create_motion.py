import streamlit as st
import numpy as np
from PIL import Image
from pages import chapter5 as c5

def create_motion_page():
    st.title("Tạo Hiệu Ứng Nhòe Chuyển Động (Motion Blur)")

    uploaded_file = st.file_uploader("Upload ảnh bất kỳ (jpg, png, bmp, tif)", type=["jpg", "jpeg", "png", "bmp", "tif"])

    if uploaded_file is not None:
        try:
            pil_image = Image.open(uploaded_file).convert("L")
            img_gray = np.array(pil_image)

            with st.spinner("Applying motion blur filter..."):
                img_filtered = c5.CreateMotion(img_gray)
            result_pil = Image.fromarray(img_filtered)

            col1, col2 = st.columns(2)
            with col1:
                st.image(pil_image, caption="Ảnh gốc (Grayscale)", use_container_width=True)
            with col2:
                st.image(result_pil, caption="Ảnh sau khi áp dụng hiệu ứng nhòe chuyển động", use_container_width=True)
        except Exception as e:
            st.error(f"Error processing image: {str(e)}")
