import cv2
import os
import time

import urllib.request as urllib
import re

path = os.getcwd()
path_photo = "d:\\IQ_photo"
path_zoom_photo =  "d:\\IQ_photo\zoom"
timestr = time.strftime("%Y_%m_%d_%H_%M") #%Y%m%d%H%M%S

print("\n------------PS:執行程式前請關閉相機APP------------")
time.sleep(3)

def create_directory(directory):
    # 檢查資料夾是否存在，如果不存在，則創建
    if not os.path.exists(directory):
        print("\n------------資料夾不存在,創建中------------")
        os.makedirs(directory)

def capture_and_save(resolution, save_path):
    # 啟動相機
    cap = cv2.VideoCapture(1)  # 0 代表默認相機，如果有多個相機，可以嘗試使用 1、2、3 等
    
    # 設定相機的分辨率
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, resolution[0])
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, resolution[1])
    
    # 檢查並設置fps（每秒幀數）
    fps = cap.get(cv2.CAP_PROP_FPS)
    print(f"\n------------現行FPS: {fps}")

    # 如果fps過高，將其設置為30
    #if fps > 30:
    #cap.set(cv2.CAP_PROP_FPS, 30)

    # 等待相機啟動
    time.sleep(1)

    # 拍照
    ret, frame = cap.read()
    print("------------開始拍照")

    # 生成檔名
    filename = f"IQ_{resolution[0]}x{resolution[1]}_{timestr}.BMP"

    # 儲存圖片到指定路徑
    save_file_path = os.path.join(save_path, filename)
    time.sleep(3)

    count = 1
    while True:
        if not os.path.exists(save_file_path):
            break
        filename = f"IQ_{resolution[0]}x{resolution[1]}_{timestr}_{count}.BMP"
        save_file_path = os.path.join(save_path, filename)
        count += 1

    cv2.imwrite(save_file_path, frame)
    
    # 檢查拍照後的resolution
    captured_resolution = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    print(f"拍照Resolution為: {captured_resolution}")

    # 顯示拍照後的圖片
    # cv2.imshow('Captured Photo', frame)
    # cv2.waitKey(0)  # 等待使用者按下任意鍵

    # 關閉相機
    cap.release()
    time.sleep(1)

    return save_file_path

def main():
    
    # 指定保存路徑
    save_path = path_photo  # 替換為你想要保存照片的路徑

    # 創建保存照片的資料夾
    create_directory(save_path)

    # 定義不同的分辨率
    #resolutions = [(3840, 2160), (2560, 1440), (1920, 1080), (1280, 720), (640, 360)]

    saved_files = []
    for resolution in resolutions:
        saved_file = capture_and_save(resolution, save_path)
        if saved_file:
            saved_files.append(saved_file)
            print(f"照片已保存到以下路徑：{saved_file}")

    if not saved_files:
        print("未成功拍攝照片。")

if __name__ == "__main__":
    main()
    # 關閉視窗
    cv2.destroyAllWindows()
    print("\n------------程式結束------------\n")
    time.sleep(3)
