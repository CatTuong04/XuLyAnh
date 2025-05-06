import streamlit as st
import numpy as np
from PIL import Image
import cv2
from pages import chapter4 as c4

def notch_reject_filter_page():
    st.title("Lọc Notch Reject trong Miền Tần Số")

    # Đặt các tham số mặc định
    rows = 256
    cols = 256
    D0 = 10.0
    centers = [(128+40, 128+30), (128-40, 128-30)]  # Tọa độ tâm nhiễu

    # Tải ảnh từ người dùng hoặc sử dụng ảnh mặc định
    uploaded_file = st.file_uploader("Tải ảnh lên ", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        # Đọc ảnh từ file tải lên
        img_pil = Image.open(uploaded_file).convert('L')  # Chuyển sang ảnh xám
        img_np = np.array(img_pil)
    else:
        # Tạo ảnh mặc định (ảnh xám đơn giản)
        img_np = np.zeros((rows, cols), dtype=np.uint8)
        img_np[::10, :] = 255  # Tạo mẫu nhiễu dạng sọc ngang
        img_pil = Image.fromarray(img_np)

    # Đảm bảo kích thước ảnh phù hợp
    if img_np.shape != (rows, cols):
        img_np = cv2.resize(img_np, (cols, rows))
        img_pil = Image.fromarray(img_np)

    # Tạo và hiển thị bộ lọc Notch Reject
    try:
        with st.spinner("Đang tạo bộ lọc Notch Reject..."):
            filter_img = c4.VisualizeNotchRejectFilter((rows, cols), centers, D0)
        filter_pil = Image.fromarray(filter_img)

        # Áp dụng bộ lọc Notch Reject lên ảnh
        filtered_img = c4.NotchRejectFilter(img_np, centers, D0)
        filtered_pil = Image.fromarray(filtered_img)

        # Hiển thị kết quả
        st.subheader("Kết quả")
        col1, col2, col3 = st.columns(3)
        
        # Đặt kích thước nhỏ hơn cho hình ảnh
        image_width = 150  # Chiều rộng cố định cho mỗi hình ảnh (đơn vị: pixel)
        
        with col1:
            st.image(img_pil, caption="Ảnh gốc", width=image_width)
        with col2:
            st.image(filter_pil, caption="Bộ lọc Notch Reject", width=image_width)
        with col3:
            st.image(filtered_pil, caption="Ảnh đã lọc", width=image_width)

    except Exception as e:
        st.error(f"Lỗi khi xử lý: {str(e)}")

if __name__ == "__main__":
    notch_reject_filter_page()