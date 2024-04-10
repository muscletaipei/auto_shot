import tkinter as tk
from tkinter import Label, OptionMenu, IntVar, Checkbutton
from tkinter.messagebox import showinfo
import os
import cv2
import time

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def capture_and_save(resolution, save_path, file_format):
    cap = cv2.VideoCapture(1)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, resolution[0])
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, resolution[1])
    time.sleep(1)
    create_directory(save_path)
    target_frames = 30
    current_frame = 0

    while current_frame < target_frames:
        ret, frame = cap.read()
        current_frame += 1
    
    fps = cap.get(cv2.CAP_PROP_FPS)
    ret, frame = cap.read()
    filename = f"IQ_{resolution[0]}x{resolution[1]}_{time.strftime('%Y%m%d_%H%M%S')}_" 
    count = 1
    
    while True:
        save_file_path = os.path.join(save_path, f"{filename}{count}.{file_format.lower()}")
        if not os.path.exists(save_file_path):
            break
        count += 1

    if file_format.lower() == 'jpg':
        cv2.imwrite(save_file_path, frame, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
    elif file_format.lower() == 'bmp':
        cv2.imwrite(save_file_path, frame)
    
    captured_resolution = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    cap.release()
    time.sleep(1)

    return save_file_path

def execute_capture(file_format_var, resolution_vars):
    output_folder = "IQ_photo"
    os.makedirs(output_folder, exist_ok=True)
    save_path = output_folder
    create_directory(save_path)
    
    resolutions = [(3840, 2160), (2560, 1440), (1920, 1080), (1280, 720), (640, 360)]
    selected_resolutions = [resolutions[i] for i, var in enumerate(resolution_vars) if var.get() == 1]
    
    file_format = 'jpg' if file_format_var == 'JPEG' else 'bmp'
    saved_files = []

    try:
        for resolution in selected_resolutions:
            saved_file = capture_and_save(resolution, save_path, file_format)
            if saved_file:
                saved_files.append(saved_file)
                print(f"照片已保存到以下路徑：{resolution} {saved_file}")
                time.sleep(2)
        if not saved_files:
            print("未成功拍攝照片。")
    except Exception as e:
        print(f"發生錯誤：{str(e)}")
    
    showinfo("Info", "照片拍攝完成。")
    print("---------------------------")
    

def main():
    root = tk.Tk()
    root.geometry("600x200")
    root.title("Capture Photos")

    # Label for file format selection
    format_label = Label(root, text="File Format:")
    format_label.place(relx=0.1, rely=0.1)

    # Dropdown menu for file format options
    format_var = tk.StringVar(root)
    format_var.set("JPEG")
    format_options = ["JPEG", "BMP"]
    format_dropdown = OptionMenu(root, format_var, *format_options)
    format_dropdown.place(relx=0.1, rely=0.2)

    # Label for resolution selection
    resolution_label = Label(root, text="Select Resolutions:")
    resolution_label.place(relx=0.5, rely=0.1)

    # Checkbuttons for resolution options
    resolution_vars = [IntVar() for _ in range(5)]
    resolution_texts = ["3840x2160", "2560x1440", "1920x1080", "1280x720", "640x360"]
    for i, text in enumerate(resolution_texts):
        resolution_checkbox = Checkbutton(root, text=text, variable=resolution_vars[i])
        resolution_checkbox.place(relx=0.5, rely=0.2 + i*0.1)

    # Capture button
    capture_button = tk.Button(root, text="Capture Photos", command=lambda: execute_capture(format_var.get(), resolution_vars))
    capture_button.place(relx=0.8, rely=0.5)
    print("---------------------------")

    root.mainloop()

if __name__ == "__main__":
    main()
