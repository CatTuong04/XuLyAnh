import cv2
import numpy as np
L = 256

def FrequencyFiltering(imgin, H):
    M, N = imgin.shape
    f = imgin.astype(np.float64)

    # Buoc 1: DFT
    F = np.fft.fft2(f)

    # Buoc 2: Shift vao center of the image
    F = np.fft.fftshift(F)

    # Buoc 3: Nhan F voi H
    G = F * H

    # Buoc 4: Shift ra tro lai
    G = np.fft.ifftshift(G)

    # Buoc 5: IDFT
    g = np.fft.ifft2(G)
    gR = g.real.copy()
    # Chuẩn hóa giá trị về [0, L-1]
    gR = np.clip(gR, 0, L-1)
    imgout = (gR / np.max(gR) * 255).astype(np.uint8) if np.max(gR) > 0 else gR.astype(np.uint8)
    return imgout

def CreateMotionFilter(M, N):
    H = np.zeros((M, N), np.complex64)
    a = 0.1
    b = 0.1
    T = 1.0
    for u in range(0, M):
        for v in range(0, N):
            phi = np.pi * (a * (u - M // 2) + b * (v - N // 2))
            if abs(phi) < 1.0e-6:
                RE = T
                IM = 0.0
            else:
                RE = (np.sin(phi) / phi * np.cos(phi)) * T if abs(phi) > 1.0e-6 else T
                IM = - (np.sin(phi) / phi * np.sin(phi)) * T if abs(phi) > 1.0e-6 else 0.0
            H.real[u, v] = RE
            H.imag[u, v] = IM
    return H

def CreateMotion(imgin):
    M, N = imgin.shape
    H = CreateMotionFilter(M, N)
    imgout = FrequencyFiltering(imgin, H)
    return imgout

def CreateInverseMotionFilter(M, N):
    H = np.zeros((M, N), np.complex64)
    a = 0.1
    b = 0.1
    T = 1.0
    for u in range(0, M):
        for v in range(0, N):
            phi = np.pi * (a * (u - M // 2) + b * (v - N // 2))
            if abs(np.sin(phi)) < 1.0e-6:
                RE = T
                IM = 0.0
            else:
                RE = (phi / np.sin(phi) * np.cos(phi)) * T if abs(np.sin(phi)) > 1.0e-6 else T
                IM = (phi / T) if abs(np.sin(phi)) > 1.0e-6 else 0.0
            H.real[u, v] = RE
            H.imag[u, v] = IM
    return H

def DeMotion(imgin):
    M, N = imgin.shape
    H = CreateInverseMotionFilter(M, N)
    imgout = FrequencyFiltering(imgin, H)
    return imgout

def CreateInverseWeinerFilter(M, N):
    H = np.zeros((M, N), np.complex64)
    a = 0.1
    b = 0.1
    T = 1.0
    for u in range(0, M):
        for v in range(0, N):
            phi = np.pi * (a * (u - M // 2) + b * (v - N // 2))
            if abs(np.sin(phi)) < 1.0e-6:
                RE = T
                IM = 0.0
            else:
                RE = (phi / np.sin(phi) * np.cos(phi)) * T if abs(np.sin(phi)) > 1.0e-6 else T
                IM = (phi / T) if abs(np.sin(phi)) > 1.0e-6 else 0.0
            H.real[u, v] = RE
            H.imag[u, v] = IM
    P = H.real**2 + H.imag**2
    K = 0.1
    H.real = H.real * P / (P + K + 1e-10)  # Thêm epsilon để tránh chia cho 0
    H.imag = H.imag * P / (P + K + 1e-10)
    return H

def DeMotionWeiner(imgin):
    M, N = imgin.shape
    H = CreateInverseWeinerFilter(M, N)
    imgout = FrequencyFiltering(imgin, H)
    return imgout