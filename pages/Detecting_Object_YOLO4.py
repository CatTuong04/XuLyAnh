import streamlit as st
import cv2
from PIL import Image
import numpy as np
import os

def detect_objects_yolo(image):
    # Fake YOLO result để demo — bạn thay bằng logic thực tế
    h, w = image.shape[:2]
    cv2.rectangle(image, (int(w*0.3), int(h*0.3)), (int(w*0.6), int(h*0.6)), (0,255,0), 2)
    cv2.putText(image, 'elephant: 0.97', (int(w*0.3), int(h*0.3)-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)
    return image

def yolo4_page():
    st.title("Điều tra đối tượng YOLOv4")

    st.markdown("### Upload Images")
    uploaded_file = st.file_uploader("Upload ảnh đối tượng", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)

        # Chuyển từ BGR (OpenCV) sang RGB (hiển thị đúng màu)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        st.image(image_rgb, caption="Ảnh gốc", width=500)

        # Nhận diện đối tượng
        if st.button("Predict"):
            result_image = detect_objects_yolo(image.copy())
            result_rgb = cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB)
            st.image(result_rgb, caption="Kết quả", width=500)
