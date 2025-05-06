import streamlit as st
import numpy as np
from PIL import Image
from pages import chapter4 as c4

def remove_moire_page():
    st.title("Xóa Nhiễu Moire (Notch Reject Filter)")

    uploaded_file = st.file_uploader("Upload ảnh bất kỳ (jpg, png, bmp, tif)", type=["jpg", "jpeg", "png", "bmp", "tif"])

    if uploaded_file is not None:
        try:
            pil_image = Image.open(uploaded_file).convert("L")
            img_gray = np.array(pil_image)

            centers = [(110, 128), (146, 128), (128, 110), (128, 146), (112, 112), (144, 144), (112, 144), (144, 112)]
            D0 = 8

            with st.spinner("Applying notch reject filter..."):
                img_filtered = c4.NotchRejectFilter(img_gray, centers=centers, D0=D0)
            result_pil = Image.fromarray(img_filtered)

            col1, col2 = st.columns(2)
            with col1:
                st.image(pil_image, caption="Ảnh gốc (Grayscale)", use_container_width=True)
            with col2:
                st.image(result_pil, caption="Ảnh sau khi xóa nhiễu Moire", use_container_width=True)
        except Exception as e:
            st.error(f"Error processing image: {str(e)}")