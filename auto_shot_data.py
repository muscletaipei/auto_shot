import cv2
import os
import time

import urllib.request as urllib
import re

path = os.getcwd()
path_photo = "d:\\IQ_photo"
path_zoom_photo =  "d:\\IQ_photo\zoom"
timestr = time.strftime("%Y%m%d_%H%M") #%Y%m%d%H%M%S

print("\n------------PS:執行程式前請關閉相機APP------------")
time.sleep(3)

def create_directory(directory):
    # 檢查資料夾是否存在，如果不存在，則創建
    if not os.path.exists(directory):
        print("\n------------資料夾不存在,創建中------------")
        os.makedirs(directory)

def capture_and_save(resolution, save_path, file_format):
    # 啟動相機
    cap = cv2.VideoCapture(1)  # 0 代表默認相機，如果有多個相機，可以嘗試使用 1、2、3 等
    
    # 設定相機的分辨率
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, resolution[0])
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, resolution[1])

    # 等待相機啟動
    time.sleep(1)

    # 確認/創建IQ_photo資料夾
    create_directory(save_path)

    # 等待resolution切換完成
    target_frames = 30  # 設定一個希望等待的帧數，這裡假設30帧，可以根據實際情況調整
    current_frame = 0

    while current_frame < target_frames:
        ret, frame = cap.read()
        current_frame += 1
    
    # 檢查並設置fps（每秒幀數）
    fps = cap.get(cv2.CAP_PROP_FPS)
    # print(f"\n------------現行FPS: {fps}")

    # 如果fps過高，將其設置為30
    #if fps > 30:
    #cap.set(cv2.CAP_PROP_FPS, 30)

    # 拍照
    ret, frame = cap.read()
    print("------------開始拍照")

    # 生成檔名
    filename = f"IQ_{resolution[0]}x{resolution[1]}_{timestr}_"

    # 找到下一個可用的編號
    count = 1
    while True:
        save_file_path = os.path.join(save_path, f"{filename}{count}.{file_format.lower()}")
        if not os.path.exists(save_file_path):
            break
        count += 1

    # 根據指定的文件格式進行保存
    if file_format.lower() == 'jpg':
        cv2.imwrite(save_file_path, frame, [int(cv2.IMWRITE_JPEG_QUALITY), 90])  # 調整 JPG 壓縮品質
    elif file_format.lower() == 'bmp':
        cv2.imwrite(save_file_path, frame)

    # count = 1
    # while True:
    #     if not os.path.exists(save_file_path):
    #         break
    #     filename = f"IQ_{resolution[0]}x{resolution[1]}_{timestr}_{count}.BMP"
    #     save_file_path = os.path.join(save_path, filename)
    #     count += 1

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
    # resolutions = [(3840, 2160), (2560, 1440), (1920, 1080), (1280, 720), (640, 360)]
    resolutions = [(3840, 2160), (1920, 1080), (1280, 720)]

    # 讓用戶選擇文件格式
    while True:
        file_format_input = input("請選擇文件格式 (1: JPG, 2: BMP): ")
        if file_format_input in ['1', '2']:
            break
        else:
            print("請輸入有效的選擇 (1 或 2)。")

    # 將用戶的選擇轉換為實際的文件格式
    file_format = 'jpg' if file_format_input == '1' else 'bmp'

    saved_files = []
    try:
        for resolution in resolutions:
            saved_file = capture_and_save(resolution, save_path, file_format)
            if saved_file:
                saved_files.append(saved_file)
                print(f"照片已保存到以下路徑：{resolution} {saved_file}")
                # 等待5秒再切換resolution
                time.sleep(2)

        if not saved_files:
            print("未成功拍攝照片。")
    except Exception as e:
        print(f"發生錯誤：{str(e)}")
 
    # 彈出視窗詢問是否再次執行
    user_input = input("是否再次執行一次？ (y/n): ")
    if user_input.lower() == 'y':
        main()
    else:
        print("\n------------程式結束------------\n")
    time.sleep(3)

if __name__ == "__main__":
    main()

