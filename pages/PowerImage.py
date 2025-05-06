import streamlit as st
import numpy as np
from PIL import Image

def power_transform(imgin, gamma):
    M, N = imgin.shape
    imgout = np.zeros((M, N), np.uint8)
    L = 256  # Giả sử ảnh 8-bit
    c = np.power(L - 1, 1 - gamma)
    for x in range(M):
        for y in range(N):
            r = imgin[x, y]
            if r == 0:
                r = 1
            s = c * np.power(r, gamma)
            imgout[x, y] = np.uint8(s)
    return imgout

def power_image_page():
    st.title("Power Transformation - Biến đổi lũy thừa (γ tùy chỉnh)")

    uploaded_file = st.file_uploader("Upload ảnh bất kỳ (jpg, png, bmp, tif)",
                                     type=["jpg", "jpeg", "png", "bmp", "tif"])

    if uploaded_file is not None:
        gamma = st.slider("Chọn giá trị gamma", min_value=0.1, max_value=10.0, value=5.0, step=0.1)

        pil_image = Image.open(uploaded_file).convert("L")
        img = np.array(pil_image)

        img_out = power_transform(img, gamma)
        result_pil = Image.fromarray(img_out)

        col1, col2 = st.columns(2)
        with col1:
            st.image(pil_image, caption="Ảnh gốc (Grayscale)", use_container_width=True)
        with col2:
            st.image(result_pil, caption=f"Ảnh sau biến đổi lũy thừa (γ = {gamma})", use_container_width=True)
