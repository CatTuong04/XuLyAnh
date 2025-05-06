import streamlit as st
import numpy as np
from PIL import Image
from pages import chapter5 as c5

def de_motion_weiner_page():
    st.title("Khôi Phục Ảnh Nhòe Chuyển Động với Bộ Lọc Wiener (De-Motion Weiner)")

    uploaded_file = st.file_uploader("Upload ảnh bất kỳ (jpg, png, bmp, tif)", type=["jpg", "jpeg", "png", "bmp", "tif"])

    if uploaded_file is not None:
        try:
            pil_image = Image.open(uploaded_file).convert("L")
            img_gray = np.array(pil_image)

            with st.spinner("Applying de-motion Weiner filter..."):
                img_filtered = c5.DeMotionWeiner(img_gray)
            result_pil = Image.fromarray(img_filtered)

            col1, col2 = st.columns(2)
            with col1:
                st.image(pil_image, caption="Ảnh gốc (Grayscale)", use_container_width=True)
            with col2:
                st.image(result_pil, caption="Ảnh sau khi khôi phục bằng bộ lọc Wiener", use_container_width=True)
        except Exception as e:
            st.error(f"Error processing image: {str(e)}")

if __name__ == "__main__":
    de_motion_weiner_page()