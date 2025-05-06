import streamlit as st
import numpy as np
from PIL import Image
from pages import chapter4 as c4  # Import chapter4 module

def frequency_filter_page():
    st.title("Lọc Thông Cao trong Miền Tần Số (Gaussian High-pass Filter)")

    uploaded_file = st.file_uploader("Upload ảnh bất kỳ (jpg, png, bmp, tif)", type=["jpg", "jpeg", "png", "bmp", "tif"])

    if uploaded_file is not None:
        try:
            # Read image and convert to grayscale
            pil_image = Image.open(uploaded_file).convert("L")
            img_gray = np.array(pil_image)

            # Apply frequency domain filter
            with st.spinner("Applying high-pass filter..."):
                img_filtered = c4.FrequencyHighPassFilter(img_gray)
            result_pil = Image.fromarray(img_filtered)

            # Display original and filtered images side by side
            col1, col2 = st.columns(2)
            with col1:
                st.image(pil_image, caption="Ảnh gốc (Grayscale)", use_container_width=True)
            with col2:
                st.image(result_pil, caption="Ảnh sau khi lọc thông cao", use_container_width=True)
        except Exception as e:
            st.error(f"Error processing image: {str(e)}")