import numpy as np
import cv2

def FrequencyHighPassFilter(img, cutoff=30):
    try:
        f = np.fft.fft2(img)
        fshift = np.fft.fftshift(f)
        
        rows, cols = img.shape
        crow, ccol = rows // 2, cols // 2
        x = np.linspace(-ccol, ccol, cols)
        y = np.linspace(-crow, crow, rows)
        X, Y = np.meshgrid(x, y)
        D = np.sqrt(X**2 + Y**2)
        H = 1 - np.exp(-(D**2) / (2 * (cutoff**2)))
        
        fshift_filtered = fshift * H
        
        f_ishift = np.fft.ifftshift(fshift_filtered)
        img_back = np.fft.ifft2(f_ishift)
        img_back = np.abs(img_back)
        
        img_back_norm = cv2.normalize(img_back, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
        
        return img_back_norm
    except Exception as e:
        raise ValueError(f"Error in FrequencyHighPassFilter: {str(e)}")

def NotchRejectFilter(img, centers, D0=8):
    try:
        # Chuyển ảnh sang miền tần số
        f = np.fft.fft2(img)
        fshift = np.fft.fftshift(f)
        
        # Kích thước ảnh
        rows, cols = img.shape
        
        # Tạo lưới tọa độ
        u = np.arange(rows)
        v = np.arange(cols)
        V, U = np.meshgrid(v, u)
        
        # Tạo bộ lọc notch reject
        H = np.ones((rows, cols), dtype=np.float32)
        for (uk, vk) in centers:
            # Khoảng cách từ điểm (U, V) đến tâm nhiễu (uk, vk)
            Dk = np.sqrt((U - uk)**2 + (V - vk)**2)
            # Khoảng cách đến điểm đối xứng (rows - uk, cols - vk)
            Dk_sym = np.sqrt((U - (rows - uk))**2 + (V - (cols - vk))**2)
            # Bộ lọc Gaussian notch reject
            H *= (1 - np.exp(-(Dk**2) / (2 * D0**2))) * (1 - np.exp(-(Dk_sym**2) / (2 * D0**2)))
        
        # Áp dụng bộ lọc lên phổ tần số
        f_filtered = fshift * H
        
        # Chuyển ngược về miền không gian
        f_ishift = np.fft.ifftshift(f_filtered)
        img_filtered = np.fft.ifft2(f_ishift)
        img_filtered = np.abs(img_filtered)
        
        # Chuẩn hóa ảnh kết quả về [0, 255]
        img_filtered = cv2.normalize(img_filtered, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
        
        # Làm mịn ảnh bằng median blur
        img_filtered_smooth = cv2.medianBlur(img_filtered, ksize=3)
        
        return img_filtered_smooth
    except Exception as e:
        raise ValueError(f"Error in NotchRejectFilter: {str(e)}")

def VisualizeNotchRejectFilter(shape, centers, D0=10):
    try:
        rows, cols = shape
        H = np.ones((rows, cols), dtype=np.float32)
        
        u = np.arange(rows)
        v = np.arange(cols)
        V, U = np.meshgrid(v, u)
        
        for (uk, vk) in centers:
            Dk = np.sqrt((U - uk)**2 + (V - vk)**2)
            Dk_sym = np.sqrt((U - (rows - uk))**2 + (V - (cols - vk))**2)
            H *= (1 - np.exp(-(Dk**2) / (2 * D0**2))) * (1 - np.exp(-(Dk_sym**2) / (2 * D0**2)))
        
        H_norm = cv2.normalize(H, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
        
        return H_norm
    except Exception as e:
        raise ValueError(f"Error in VisualizeNotchRejectFilter: {str(e)}")