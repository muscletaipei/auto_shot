
import os
import time
import cv2

path = os.getcwd()
path_photo = "d:\\IQ_photo"
path_zoom_photo =  "d:\\IQ_photo\zoom"
timestr = time.strftime("%m%d") #%Y%m%d%H%M%S

# def scaling(img_path): #影像縮放方法
	
# 	img = cv2.imread(img_path)

# 	if img is None:
# 		sys.exit("無法讀取影像...")

# 	#影像放大
# 	#方法1
# 	res = cv2.resize(img,None,fx=1.5, fy=1.5, interpolation = cv2.INTER_CUBIC)
	
# 	#方法2
# 	height, width = img.shape[:2]
# 	res2 = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)
# 	print(img.shape)
# 	cv2.imshow('res',res)
# 	cv2.imshow('res2',res2)
	
# 	k = cv2.waitKey(0)
# 	cv2.destroyAllWindows() 

# 讀取圖片
img = cv2.imread(path_photo + '1.jpg')

# 取得原始圖片的高和寬
height, width = img.shape[:2]

# 將圖片放大為原來的兩倍
res2 = cv2.resize(img, (2 * width, 2 * height), interpolation=cv2.INTER_CUBIC)

# 顯示原始圖片和放大後的圖片
cv2.imshow('Original', img)
cv2.imshow('Resized and Enlarged', res2)

# 將放大後格放的圖片儲存到指定位置
output_path = path_photo + '2.jpg'  # 替換為你想要保存的路徑和檔名
cv2.imwrite(output_path, res2)

# 等待按鍵關閉視窗
cv2.waitKey(0)
cv2.destroyAllWindows()



