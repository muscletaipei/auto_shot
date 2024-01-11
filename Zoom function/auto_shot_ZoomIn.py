import cv2
import os
import time

path = os.getcwd()
path_photo = "d:\\IQ_photo" 
print("please create folder to d:/IQ_photo\n")
print("\n開始拍照\n儲存路經 "+ path_photo)
timestr = time.strftime("%Y%m%d%H%M%S")


def capture_and_zoom(resolution, save_path, zoom_factor):
    # 啟動相機
    cap = cv2.VideoCapture(0)  # 0 代表默認相機，如果有多個相機，可以嘗試使用 1、2、3 等

    # 設定相機的分辨率
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, resolution[0])
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, resolution[1])

    # 等待相機啟動
    time.sleep(2)

    # 拍照
    ret, frame = cap.read()

    # 進行200%的zoom in
    zoomed_frame = cv2.resize(frame, None, fx=zoom_factor, fy=zoom_factor, interpolation=cv2.INTER_CUBIC)

    # 生成檔名
    filename = f"captured_photo_{resolution[0]}x{resolution[1]}_{int(zoom_factor * 100)}percent_{int(time.time())}.jpg"

    # 儲存圖片到指定路徑
    save_file_path = os.path.join(save_path, filename)
    count = 1
    while os.path.exists(save_file_path):
        filename = f"captured_photo_{resolution[0]}x{resolution[1]}_{int(zoom_factor * 100)}percent_{int(time.time())}_{count}.jpg"
        save_file_path = os.path.join(save_path, filename)
        count += 1

    cv2.imwrite(save_file_path, zoomed_frame)

    # 關閉相機
    cap.release()

    return save_file_path

# 定義不同的分辨率
resolutions = [(3840, 2160), (1920, 1080), (1280, 720)]

# 指定保存路徑
save_path = path_photo  # 替換為你想要保存照片的路徑

# Zoom因子 (1.0 表示原始大小，2.0 表示200%的zoom in)
zoom_factor = 2.0

# 逐一拍照
saved_files = []
for resolution in resolutions:
    saved_file = capture_and_zoom(resolution, save_path, zoom_factor)
    saved_files.append(saved_file)

print("照片已保存到以下路徑：", saved_files)






