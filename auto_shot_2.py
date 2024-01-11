import cv2
import os
import time
import sys

path = os.getcwd()
path_photo = "d:\\IQ_photo"
path_zoom_photo =  "d:\\IQ_photo\zoom"
timestr = time.strftime("%m%d") #%Y%m%d%H%M%S

print("\n------------PS:執行程式前請關閉相機APP------------\n")
time.sleep(3)
print("------------開始拍照------------\n")

def create_directory(directory):
    # 檢查資料夾是否存在，如果不存在，則創建
    if not os.path.exists(directory):
        os.makedirs(directory)
        print("------------創建IQ_Photo資料夾------------\n")

def capture_and_save(resolution, save_path):
    # 啟動相機
    cap = cv2.VideoCapture(1)  # 0 代表默認相機，如果有多個相機，可以嘗試使用 1、2、3 等

    # 設定相機的分辨率
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, resolution[0])
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, resolution[1])

    # 拍照
    ret, frame = cap.read()

    # 生成檔名
    filename = f"{resolution[0]}x{resolution[1]}_{timestr}_{int(time.time())}.jpg"

    # 儲存圖片到指定路徑
    save_file_path = os.path.join(save_path, filename)
    # count = 1
    while os.path.exists(save_file_path):
        save_file_path = os.path.join(save_path, filename)
        # count += 1

    cv2.imwrite(save_file_path, frame)
    # cap.release()
    #關閉視窗
    cv2.destroyAllWindows()
    return save_file_path

def main():
    save_path = path_photo  # 替換為你想要保存照片的路徑

    create_directory(save_path)

    # 定義不同的分辨率
    #resolutions = [(3840, 2160), (2560, 1440), (1920, 1080), (1280, 720), (640, 360)]
    resolutions = [(3840, 2160), (1920, 1080), (1280, 720)]

    saved_files = []
    for resolution in resolutions:
        saved_file = capture_and_save(resolution, save_path)
        if saved_file:
            saved_files.append(saved_file)
            print(f"照片已保存到以下路徑：{resolution} {saved_file}")
            time.sleep(6)

    if not saved_files:
        print("未成功拍攝照片。")

if __name__ == "__main__":
    main()
    print("\n------------程式結束------------\n")
    time.sleep(3)





