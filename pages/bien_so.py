import streamlit as st
import cv2
import numpy as np
from ultralytics import YOLO
import os

# Tải mô hình YOLOv8 Tiny
@st.cache_resource
def load_yolo_model():
    weights_path = "pages/Source/CacBTKhac/best.pt"
    if not os.path.exists(weights_path):
        st.error(f"Tệp trọng số không tồn tại: {os.path.abspath(weights_path)}")
        return None
    return YOLO(weights_path)

# Hàm xử lý khung hình để làm mờ biển số
def process_frame(img, model):
    results = model(img)
    detections = results[0].boxes.data.cpu().numpy()
    for det in detections:
        x1, y1, x2, y2, conf, cls = det
        if conf > 0.3 and int(cls) in [0, 1]:  # Xử lý cả BSD (0) và BSV (1)
            x1, y1, x2, y2 = max(0, int(x1)), max(0, int(y1)), int(x2), int(y2)
            if x2 > x1 and y2 > y1 and x2 <= img.shape[1] and y2 <= img.shape[0]:
                roi = img[y1:y2, x1:x2]
                blurred = cv2.GaussianBlur(roi, (51, 51), 10)
                img[y1:y2, x1:x2] = blurred
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    return img

# Giao diện Streamlit
def bien_so_page():
    st.title("Nhận diện và làm mờ biển số xe")
    st.markdown("**Webcam sẽ tự động làm mờ các biển số phát hiện được.**")

    # Tải mô hình YOLOv8 Tiny
    model = load_yolo_model()
    if model is None:
        return

    # Khởi tạo webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        st.error("Không thể truy cập webcam. Vui lòng kiểm tra kết nối webcam hoặc thử chỉ số khác (1, 2, ...).")
        return

    # Tạo placeholder để hiển thị video
    frame_placeholder = st.empty()

    # Nút dừng
    stop_button = st.button("Dừng")

    # Vòng lặp video
    while not stop_button:
        ret, frame = cap.read()
        if not ret:
            st.warning("Không thể đọc khung hình từ webcam.")
            break

        # Giảm độ phân giải để tăng tốc
        frame = cv2.resize(frame, (640, 480))

        # Xử lý khung hình để làm mờ biển số
        processed_frame = process_frame(frame, model)

        # Chuyển đổi khung hình sang định dạng RGB
        processed_frame_rgb = cv2.cvtColor(processed_frame, cv2.COLOR_BGR2RGB)

        # Hiển thị khung hình
        frame_placeholder.image(processed_frame_rgb, channels="RGB", use_container_width=True)

    # Giải phóng webcam
    cap.release()

