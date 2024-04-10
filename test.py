import cv2
import os
import time

path_photo = "d:\\IQ_photo"
path_zoom_photo = "d:\\IQ_photo\\zoom"
timestr = time.strftime("%m%d")  # %Y%m%d%H%M%S

# 變數來存儲zoom的初始值
zoom_value = 1

# 滑鼠事件回調函數
def mouse_callback(event, x, y, flags, param):
    global zoom_value

    if event == cv2.EVENT_MOUSEWHEEL:
        # 判斷滑鼠滾輪向前還是向後滾動
        if flags > 0:
            # 向前滾動，zoom in
            zoom_value += 0.1
        else:
            # 向後滾動，zoom out
            zoom_value -= 0.1

# 創建一個窗口，用於顯示相機畫面
cv2.namedWindow('Camera Preview')
cv2.setMouseCallback('Camera Preview', mouse_callback)

def create_directory(directory):
    # 檢查資料夾是否存在，如果不存在，則創建
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"------------創建{directory}資料夾------------\n")

def capture_and_save(resolution, save_path, file_format):
    global zoom_value

    # 啟動相機
    cap = cv2.VideoCapture(1)

    # 設定相機的分辨率
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, resolution[0])
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, resolution[1])

    # 等待相機啟動
    time.sleep(2)

    # 確認/創建IQ_photo資料夾
    create_directory(save_path)

    # 等待resolution切換完成
    target_frames = 30
    current_frame = 0

    while current_frame < target_frames:
        ret, frame = cap.read()
        current_frame += 1

    # 拍照
    ret, frame = cap.read()

    # 生成檔名
    filename = f"{resolution[0]}x{resolution[1]}_{timestr}_{int(time.time())}_"

    # 找到下一個可用的編號
    count = 1
    while True:
        save_file_path = os.path.join(save_path, f"{filename}{count}.{file_format.lower()}")
        if not os.path.exists(save_file_path):
            break
        count += 1

    # Zoom in
    frame = cv2.resize(frame, None, fx=zoom_value, fy=zoom_value)

    # 根據指定的文件格式進行保存
    if file_format.lower() == 'jpg':
        cv2.imwrite(save_file_path, frame, [int(cv2.IMWRITE_JPEG_QUALITY), 90])  # 調整 JPG 壓縮品質
    elif file_format.lower() == 'bmp':
        cv2.imwrite(save_file_path, frame)

    # 關閉相機
    cap.release()
    # 關閉視窗
    cv2.destroyAllWindows()

    return save_file_path

def main():
    global zoom_value
    save_path = path_photo

    create_directory(save_path)

    # 定義不同的分辨率
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
                time.sleep(5)

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

if __name__ == "__main__":
    main()

