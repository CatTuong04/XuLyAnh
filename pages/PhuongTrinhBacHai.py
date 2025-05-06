import math
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Khởi tạo session state nếu chưa tồn tại
if "nhap_a" not in st.session_state:
    st.session_state["nhap_a"] = 0.0
if "nhap_b" not in st.session_state:
    st.session_state["nhap_b"] = 0.0
if "nhap_c" not in st.session_state:
    st.session_state["nhap_c"] = 0.0

# Vẽ đồ thị parabol
def DrawPhuongTrinh(a, b, c):
    x = np.linspace(-10, 10, 400)
    y = a * x**2 + b * x + c
    fig, ax = plt.subplots()
    ax.plot(x, y, label="Đồ thị: y = ax² + bx + c")
    ax.axhline(0, color='gray', linewidth=0.5)
    ax.axvline(0, color='gray', linewidth=0.5)
    ax.grid(True)
    ax.legend()
    
    # Giới hạn trục y từ -10 đến 10
    ax.set_ylim(-10, 10)
    
    # Đặt các nhãn trục x là số nguyên, bước nhảy là 1
    ax.set_xticks(np.arange(-10, 11, 1))
    
    # Đặt các nhãn trục y là số nguyên, bước nhảy là 1
    ax.set_yticks(np.arange(-10, 11, 1))
    
    return fig, ax  # Trả về cả fig và ax

def DrawPoint(x, a, b, c, ax):  # Thêm tham số ax để vẽ trực tiếp trên trục
    y = a * x**2 + b * x + c
    if -10 <= y <= 10:  # Chỉ vẽ điểm nếu y nằm trong phạm vi hiển thị
        ax.plot(x, y, marker="o", markersize=6, color="red")

def clear_input():
    st.session_state["nhap_a"] = 0.0
    st.session_state["nhap_b"] = 0.0
    st.session_state["nhap_c"] = 0.0

def gptb2_logic(a, b, c):
    info = []
    if a == 0:
        if b == 0:
            if c == 0:
                ket_qua = 'Phương trình có vô số nghiệm.'
            else:
                ket_qua = 'Phương trình vô nghiệm.'
        else:
            x = -c / b
            info.append(x)
            ket_qua = f'Phương trình có nghiệm: x = {x:.2f}'
    else:
        delta = b**2 - 4 * a * c
        if delta < 0:
            ket_qua = 'Phương trình vô nghiệm.'
        elif delta == 0:
            x = -b / (2 * a)
            info.append(x)
            ket_qua = f'Phương trình có nghiệm kép: x = {x:.2f}'
        else:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            info.extend([x1, x2])
            ket_qua = f'Phương trình có 2 nghiệm: x₁ = {x1:.2f}, x₂ = {x2:.2f}'
    info.append(ket_qua)
    return info

# Hàm chính để hiển thị trang
def gptb2():
    st.title("Giải phương trình bậc hai")

    col1, col2 = st.columns([1.5, 1])  # col1: hình bên trái, col2: nhập liệu bên phải

    with col2:
        a = st.number_input("Nhập hệ số a", key="nhap_a")
        b = st.number_input("Nhập hệ số b", key="nhap_b")
        c = st.number_input("Nhập hệ số c", key="nhap_c")

        col_giai, col_xoa = st.columns(2)
        with col_giai:
            btn_giai = st.button("Giải")
        with col_xoa:
            st.button("Xóa", on_click=clear_input)

    with col1:
        fig, ax = DrawPhuongTrinh(a, b, c)  # Lấy cả fig và ax

        if btn_giai:
            kq = gptb2_logic(a, b, c)
            st.markdown(f"**Kết quả:** {kq[-1]}")
            for x in kq[:-1]:
                DrawPoint(x, a, b, c, ax)  # Truyền ax vào DrawPoint để vẽ điểm

        st.pyplot(fig)

