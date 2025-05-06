import streamlit as st

def cs_sidebar():
    with st.sidebar:
        st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
        st.image("assets/logo.jpg", width=200)
        st.markdown("## Image Processing")
        st.markdown("### Các Bài Học")

        # Các nút chính – gán trang vào session_state
        if st.button("Giải phương trình."):
            st.session_state["page"] = "gptb2"

        if st.button("Nhận diện 5 khuôn mặt."):
            st.session_state["page"] = "face_detection"

        if st.button("Nhận diện đối tượng yolo4."):
            st.session_state["page"] = "yolo4"

        if st.button("Nhận diện chữ số NIST."):
            st.session_state["page"] = "nist"

        if st.button("Xác định ít nhất 5 đối tượng trái cây."):
            st.session_state["page"] = "detect_objects"

        st.markdown("---")
        st.markdown("### Xử lý ảnh – Biến đổi độ sáng và lọc")
        option_to_page = {
        "1. Negative Image": "negative_image",
        "2. Logarithmic Image": "log_image",
        "3. Lũy thừa Image": "power_image",
        "4. Biến đổi tuyến tính": "linear_transform",
        "5. Histogram": "histogram",
        "6. Cân bằng Histogram": "hist_equal",
        "7. Cân bằng Histogram của ảnh màu": "hist_equal_color",
        "8. Local Histogram": "local_hist",
        "9. Thống kê Histogram": "hist_stat",
        "10. Lọc Box": "smooth_box",
        "11. Lọc Gauss": "smooth_gauss",
        "12. Phân Ngưỡng": "threshold",
        "13. Lọc Median": "median_filter",
        "14. Sharpen": "sharp",
        "15. Gradient": "gradient"
        }
        options = ["Chọn nội dung"] + list(option_to_page.keys())

        def set_page():
            selected = st.session_state["selected_bai"]
            if selected != "Chọn nội dung":
                st.session_state["page"] = option_to_page[selected]

        st.selectbox(
            "Chọn bài:", options,
            key="selected_bai",
            on_change=set_page
        )

        st.markdown("### Chương 4")
        freq_option_to_page = {
            "1. Spectrum": "spectrum",
            "2. Lọc trong miền tần số": "freq_filter",
            "3. Vẽ bộ lọc note-reject": "notch_reject_filter",
            "4. Xóa nhiễu Moire": "remove_moire"
        }
        freq_options = ["Chọn nội dung"] + list(freq_option_to_page.keys())

        def set_freq_page():
            selected = st.session_state["selected_freq_bai"]
            if selected != "Chọn nội dung":
                st.session_state["page"] = freq_option_to_page[selected]

        st.selectbox(
            "Chọn bài:", freq_options,
            key="selected_freq_bai",
            on_change=set_freq_page
        )


        st.markdown("### Chương 5")
        noise_option_to_page = {
            "1. Tạo hiệu ứng mờ chuyển động.": "create_motion",
            "2. Khôi phục ảnh bị mờ chuyển động bằng bộ lọc nghịch đảo.": "de_motion",
            "3. Khôi phục ảnh bị mờ chuyển động bằng bộ lọc Wiener.": "de_motion_weiner"
        }
        noise_options = ["Chọn nội dung"] + list(noise_option_to_page.keys())

        def set_noise_page():
            selected = st.session_state["selected_noise_bai"]
            if selected != "Chọn nội dung":
                st.session_state["page"] = noise_option_to_page[selected]

        st.selectbox(
            "Chọn bài (Nhiễu):", noise_options,
            key="selected_noise_bai",
            on_change=set_noise_page
        )


        st.markdown("### Xử lý hình thái")
        grain_option_to_page = {
            "1. PhiLeGa": "philega",
            "2. HatGao": "hatgao",
            "3. Khác": "khac"
        }
        grain_options = ["Chọn nội dung"] + list(grain_option_to_page.keys())

        def set_grain_page():
            selected = st.session_state["selected_grain_bai"]
            if selected != "Chọn nội dung":
                st.session_state["page"] = grain_option_to_page[selected]

        st.selectbox(
            "Chọn bài (Nhận diện hạt):", grain_options,
            key="selected_grain_bai",
            on_change=set_grain_page
        )


        st.markdown("### Các Bài Tập Làm Thêm")
        if st.button("Kiểm tra biển số xe"):
            st.session_state["page"] = "bien_so"

        if st.button("Phân biệt giới tính"):
            st.session_state["page"] = "ve_khuon_mat"

        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown("""
        <div style="text-align: left;">
            <p>22110263 Nguyễn Võ Cát Tường</p>
            <p>22110137 Nguyễn Thanh Hiền</p>
        </div>
        """, unsafe_allow_html=True)
