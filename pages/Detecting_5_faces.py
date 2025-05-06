import cv2 as cv
import numpy as np
import joblib
import streamlit as st
from sklearn.svm import SVC


def khuonmat():
    st.title("Nhận dạng khuôn mặt 5 người")

    # Khởi tạo session_state nếu chưa có
    if "stop" not in st.session_state:
        st.session_state.stop = True
    if "running" not in st.session_state:
        st.session_state.running = False
    if "mode" not in st.session_state:
        st.session_state.mode = None

    # ======= Các hàm xử lý nút =======
    def start_realtime():
        st.session_state.stop = False
        st.session_state.running = True
        st.session_state.mode = "realtime"

    def start_video():
        st.session_state.stop = False
        st.session_state.running = True
        st.session_state.mode = "video"

    def stop_running():
        st.session_state.stop = True
        st.session_state.running = False
        st.session_state.mode = None

    # ======= Giao diện nút =======
    col0, col1, col2, col3, col4 = st.columns([1, 2, 2, 2, 1])

    with col1:
        st.button("Real Time", type="primary", on_click=start_realtime)
    with col2:
        st.button("Video", type="primary", on_click=start_video)
    with col3:
        if st.session_state.running:
            st.button("Stop", type="primary", on_click=stop_running)

    # Nếu không đang chạy thì dừng lại
    if not st.session_state.running:
        return

    # ======= Xử lý nhận diện khuôn mặt =======
    svc = joblib.load('./pages/Source/KhuonMat/svc.pkl')
    mydict = ['CatTuong', 'ThanhHien']
    color = [(0, 255, 0), (255, 0, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255)]

    detector = cv.FaceDetectorYN.create(
        './pages/Source/KhuonMat/face_detection_yunet_2023mar.onnx', "",
        (320, 320), 0.9, 0.3, 5000
    )
    recognizer = cv.FaceRecognizerSF.create(
        './pages/Source/KhuonMat/face_recognition_sface_2021dec.onnx', ""
    )

    FRAME_WINDOW = st.image([])

    # Chọn nguồn video
    source = 0 if st.session_state.mode == "realtime" else './images/video_predict.mp4'
    cap = cv.VideoCapture(source)

    frameWidth = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    frameHeight = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
    detector.setInputSize((frameWidth, frameHeight))
    tm = cv.TickMeter()

    while cap.isOpened() and not st.session_state.stop:
        ret, frame = cap.read()
        if not ret:
            break

        tm.start()
        faces = detector.detect(frame)
        tm.stop()

        y = 50
        if faces[1] is not None:
            for face_info in faces[1]:
                face_align = recognizer.alignCrop(frame, face_info)
                face_feature = recognizer.feature(face_align)
                test_predict = svc.predict(face_feature)

                result = mydict[test_predict[0]]
                coords = face_info[:-1].astype(np.int32)

                cv.putText(frame, result, (1, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, color[test_predict[0]], 2)
                y += 20
                cv.rectangle(frame, (coords[0], coords[1]),
                             (coords[0]+coords[2], coords[1]+coords[3]), color[test_predict[0]], 2)

        cv.putText(frame, 'FPS: {:.2f}'.format(tm.getFPS()), (1, 16),
                   cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        FRAME_WINDOW.image(frame, channels='BGR')

    cap.release()
    cv.destroyAllWindows()
