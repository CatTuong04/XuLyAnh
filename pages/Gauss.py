import streamlit as st
import numpy as np
import cv2
from PIL import Image

def smooth_gauss_page():
    st.title("Lọc ảnh bằng Gaussian Filter (Adaptive Division)")

    uploaded_file = st.file_uploader("Upload ảnh (jpg, png, bmp, tif)", type=["jpg", "jpeg", "png", "bmp", "tif"])

    if uploaded_file is not None:
        # Đọc và chuyển ảnh sang grayscale
        pil_image = Image.open(uploaded_file).convert("L")
        img_gray = np.array(pil_image)

        # Bắt đầu xử lý Gaussian như mã OpenCV gốc
        blurred = cv2.GaussianBlur(img_gray, (1025, 1025), 128.0)
        M, N = img_gray.shape
        temp2 = np.zeros((M, N), np.float32)
        imgout = np.zeros((M, N), np.uint8)

        # Chia ảnh gốc cho ảnh làm mờ
        for x in range(M):
            for y in range(N):
                a = img_gray[x, y]
                b = blurred[x, y]
                if b != 0:
                    s = 1.0 * a / b
                else:
                    s = 0
                temp2[x, y] = np.float32(s)

        # Tìm giá trị max để chuẩn hóa
        min_val, max_val, _, _ = cv2.minMaxLoc(temp2)

        # Chuẩn hóa và gán vào ảnh đầu ra
        for x in range(M):
            for y in range(N):
                r = temp2[x, y]
                s = 255 * r / max_val
                imgout[x, y] = np.uint8(s)

        result_pil = Image.fromarray(imgout)

        # Hiển thị 2 cột: ảnh gốc và ảnh đã xử lý
        col1, col2 = st.columns(2)
        with col1:
            st.image(pil_image, caption="Ảnh gốc (Grayscale)", use_container_width=True)
        with col2:
            st.image(result_pil, caption="Ảnh sau khi xử lý Gaussian Adaptive", use_container_width=True)
