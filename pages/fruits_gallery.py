import streamlit as st
from ultralytics import YOLO
from PIL import Image

# Load YOLO model chỉ một lần
@st.cache_resource
def load_yolo_model():
    return YOLO("pages/Source/TraiCay/best.pt")

# Giao diện Streamlit
def fruit_page():
    st.title("Nhận diện trái cây bằng YOLOv8")

    uploaded_file = st.file_uploader("Upload ảnh 6 loại trái cây (jpg, png)", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")  # PIL image

        # Tạo hai cột để hiển thị ảnh gốc và ảnh kết quả cạnh nhau
        col1, col2 = st.columns(2)

        # Hiển thị ảnh gốc trong cột 1
        with col1:
            st.image(image, caption="Ảnh gốc", use_container_width=True)

        if st.button("Predict"):
            model = load_yolo_model()
            results = model.predict(source=image)

            # Lấy ảnh có kết quả
            res_image = results[0].plot()  # numpy array có khung và nhãn
            res_pil = Image.fromarray(res_image)  # chuyển thành ảnh PIL

            # Hiển thị ảnh kết quả trong cột 2
            with col2:
                st.image(res_pil, caption="Kết quả nhận diện", use_container_width=True)