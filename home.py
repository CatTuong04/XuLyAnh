# Các import ban đầu
import streamlit as st
from PIL import Image
from library.bosung_streamlit.sidebar import cs_sidebar
from pages.PhuongTrinhBacHai import gptb2
from pages.Detecting_5_faces import khuonmat
from pages.Detecting_Object_YOLO4 import yolo4_page
from pages.NISTS_Numbers_Identification import nist_page
from pages.fruits_gallery import fruit_page
from pages.NegativeImage import power_image_page
from pages.LogaritImage import logarithmic_image_page
from pages.PowerImage import power_image_page
from pages.LinearImage import piecewise_linear_page
from pages.Histogram import histogram_page
from pages.HisEqual import his_equal_page
from pages.HisColorEqual import his_equal_color_page
from pages.LocalHistogram import local_hist_page
from pages.HistStat import hist_stat_page
from pages.Box import smooth_box_page
from pages.Gauss import smooth_gauss_page
from pages.Hubble import threshold_page
from pages.Median import median_filter_page
from pages.Sharp import sharpen_image_page
from pages.Gradient import gradient_image_page
from pages.Spectrum import spectrum_page
from pages.loc_mien_tan_so import frequency_filter_page
from pages.remove_moire import remove_moire_page
from pages.notch_reject_filter import notch_reject_filter_page
from pages.bien_so import bien_so_page
from pages.ve_khuon_mat import classification_page
from pages.create_motion import create_motion_page
from pages.de_motion import de_motion_page
from pages.de_motion_weiner import de_motion_weiner_page


# Cấu hình giao diện
st.set_page_config(page_title="Image Processing", layout="wide")

hide_default_format = """
    <style>
        [data-testid="stSidebarNav"] {
            display: none;
        }
    </style>
"""
st.markdown(hide_default_format, unsafe_allow_html=True)

# Sidebar điều hướng
cs_sidebar()

# Điều hướng trang
if st.session_state.get("page") == "gptb2":
    gptb2()
elif st.session_state.get("page") == "face_detection":
    khuonmat()
elif st.session_state.get("page") == "yolo4":
    yolo4_page()
elif st.session_state.get("page") == "nist":
    nist_page()
elif st.session_state.get("page") == "detect_objects":
    fruit_page()
elif st.session_state.get("page") == "negative_image":
    power_image_page()
elif st.session_state.get("page") == "log_image":
    logarithmic_image_page()
elif st.session_state.get("page") == "power_image":
    power_image_page()
elif st.session_state.get("page") == "linear_transform":
    piecewise_linear_page()
elif st.session_state.get("page") == "histogram":
    histogram_page()
elif st.session_state.get("page") == "hist_equal":
    his_equal_page()
elif st.session_state.get("page") == "hist_equal_color":
    his_equal_color_page()
elif st.session_state.get("page") == "local_hist":
    local_hist_page()
elif st.session_state.get("page") == "hist_stat":
    hist_stat_page()
elif st.session_state.get("page") == "smooth_box":
    smooth_box_page() 
elif st.session_state.get("page") == "smooth_gauss":
    smooth_gauss_page() 
elif st.session_state.get("page") == "threshold":
    threshold_page() 
elif st.session_state.get("page") == "median_filter":
    median_filter_page()
elif st.session_state.get("page") == "sharp":
    sharpen_image_page()
elif st.session_state.get("page") == "gradient":
    gradient_image_page()
elif st.session_state.get("page") == "spectrum":
    spectrum_page()
elif st.session_state.get("page") == "freq_filter":
    frequency_filter_page()
elif st.session_state.get("page") == "remove_moire":
    remove_moire_page()
elif st.session_state.get("page") == "notch_reject_filter":
    notch_reject_filter_page()
elif st.session_state.get("page") == "bien_so":
    bien_so_page()
elif st.session_state.get("page") == "ve_khuon_mat":
    classification_page()
elif st.session_state.get("page") == "create_motion":
    create_motion_page()
elif st.session_state.get("page") == "de_motion":
    de_motion_page()
elif st.session_state.get("page") == "de_motion_weiner":
    de_motion_weiner_page()
else:
    # Mặc định: Trang chủ với tên + hình ảnh
    st.markdown("""
    <div style='display: flex; justify-content: center; align-items: center; gap: 20px;'>
        <div style='text-align: left;'>
            <h4 style='margin: 4px;'>22110263 Nguyễn Võ Cát Tường</h4>
            <h4 style='margin: 4px;'>22110137 Nguyễn Thanh Hiền</h4>
        </div>
        <div style='border-left: 2px solid #aaa; padding-left: 20px;'>
            <h2 style='color: #4A90E2; margin: 5px;'>Xử lý ảnh</h2>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Hiển thị hình ảnh
    image_paths = [
        "assets/images/einstein.jpg",
        "assets/images/mona_lisa.jpg",
        "assets/images/clouds.jpg",
        "assets/images/lena.png",
        "assets/images/starry_night.jpg",
        "assets/images/squirrel.jpg"
    ]
    target_size = (200, 200)
    images = [Image.open(p).resize(target_size) for p in image_paths]
    rows = [st.columns(3), st.columns(3)]

    for idx, img in enumerate(images):
        row = rows[idx // 3]
        with row[idx % 3]:
            st.image(img, width=200)
            if idx % 3 == 2:
                st.markdown("<br>", unsafe_allow_html=True)
