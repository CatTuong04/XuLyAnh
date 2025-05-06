import streamlit as st
import cv2
import mediapipe as mp
import numpy as np

# MediaPipe Face Detection
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils
face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.5)

# Đường dẫn tới các file mô hình
GENDER_MODEL = "D:/HOC_TAP/HK01-2025/BAITAP/XLAS/CuoiKy/Coding/pages/source/CacBTKhac/gender_deploy.prototxt"
GENDER_WEIGHTS = "D:/HOC_TAP/HK01-2025/BAITAP/XLAS/CuoiKy/Coding/pages/source/CacBTKhac/gender_net.caffemodel"


# Tải mô hình
gender_net = cv2.dnn.readNetFromCaffe(GENDER_MODEL, GENDER_WEIGHTS)

# Danh sách nhãn
gender_list = ['Male', 'Female']

# Streamlit Interface
def classification_page():
    st.title("Phân biệt giới tính bằng Webcam")
    st.markdown("Ứng dụng này sử dụng webcam và mô hình học sâu để nhận diện và phân biệt giới tính dựa trên khuôn mặt.")

    # Stop button
    stop_button = st.button("Dừng")

    # Initialize webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        st.error("Không mở được webcam.")
        return

    # Placeholder for video frame
    frame_placeholder = st.empty()

    while cap.isOpened() and not stop_button:
        ret, frame = cap.read()
        if not ret:
            st.warning("Không thể đọc khung hình.")
            break

        # Convert frame to RGB for MediaPipe
        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_detection.process(img_rgb)

        if results.detections:
            for detection in results.detections:
                # Get bounding box
                bbox = detection.location_data.relative_bounding_box
                h, w, _ = frame.shape
                x1 = int(bbox.xmin * w)
                y1 = int(bbox.ymin * h)
                x2 = int((bbox.xmin + bbox.width) * w)
                y2 = int((bbox.ymin + bbox.height) * h)

                # Ensure bounding box is within frame
                x1, y1 = max(0, x1), max(0, y1)
                x2, y2 = min(w, x2), min(h, y2)

                # Crop face
                face_img = frame[y1:y2, x1:x2]
                if face_img.size == 0:
                    continue

                # Preprocess for gender classification (resize to 227x227 as required by the model)
                blob = cv2.dnn.blobFromImage(face_img, 1.0, (227, 227), (78.4263377603, 87.7689143744, 114.895847746), swapRB=False)

                # Gender classification
                gender_net.setInput(blob)
                gender_preds = gender_net.forward()
                gender = gender_list[gender_preds[0].argmax()]
                confidence = gender_preds[0].max()

                # Draw bounding box and label
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                label = f"{gender} ({confidence:.2f})"
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        # Convert frame to RGB for Streamlit display
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_placeholder.image(frame_rgb, channels="RGB", use_container_width=True)

    # Release webcam
    cap.release()