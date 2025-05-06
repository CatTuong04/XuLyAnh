import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from io import BytesIO


def nist_page():
    st.title("Nhận diện chữ số Nist")

    digits = load_digits()
    X_train, X_test, y_train, y_test = train_test_split(
        digits.data, digits.target, test_size=0.2, random_state=42)
    model = SVC(gamma=0.001)
    model.fit(X_train, y_train)

    if 'nist_image' not in st.session_state:
        st.session_state.nist_image = None
        st.session_state.nist_labels = None
        st.session_state.show_predict = False

    if st.button("Tạo ảnh", use_container_width=True):
        st.session_state.nist_image = digits.images[:64]
        st.session_state.nist_labels = None
        st.session_state.show_predict = True

    if st.session_state.nist_image is not None:
        fig, axs = plt.subplots(8, 8, figsize=(4, 4), dpi=100)
        for i in range(8):
            for j in range(8):
                axs[i, j].imshow(st.session_state.nist_image[i * 8 + j],
                    cmap='gray', interpolation='nearest')
                axs[i, j].axis('off')
        plt.subplots_adjust(wspace=0.05, hspace=0.05, left=0, right=1, top=1, bottom=0)

        # Lưu ảnh vào bộ nhớ
        buf = BytesIO()
        fig.savefig(buf, format="png", bbox_inches="tight", pad_inches=0)
        buf.seek(0)
        plt.close(fig)  # tránh hiện lại plot dư thừa

        # Hiển thị ảnh bằng st.image với width nhỏ
        st.image(buf, width=150)  # bạn có thể thử 250, 200 tùy ý


    if st.session_state.show_predict:
        if st.button("Nhận dạng", use_container_width=True):
            data = st.session_state.nist_image.reshape((64, -1))
            result = model.predict(data)
            st.session_state.nist_labels = result
            st.session_state.show_predict = False

    if st.session_state.nist_labels is not None:
        st.markdown("### Kết quả nhận dạng:")
        result_matrix = st.session_state.nist_labels.reshape((8, 8))
        styled_rows = ""
        for row in result_matrix:
                line = " ".join(str(x) for x in row)
                styled_rows += f"<p style='margin:0; line-height:1.1; font-family:monospace;'>{line}</p>\n"
        st.markdown(styled_rows, unsafe_allow_html=True)

