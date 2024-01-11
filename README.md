## OpenCV:
## Feature
1. 啟動相機，設定分辨率和等待相機啟動。
2. 檢查相機的 fps，如果過高，設置為 30。
3. 拍照並保存到指定路徑，生成檔名時考慮避免檔案名稱重複。
4. 檢查拍照後的 resolution。
5. 顯示拍照後的圖片（註釋）。
6. 關閉相機和視窗，並延遲 1 秒。
7. 使用PyInstaller或cx_Freeze等工具來將Python腳本打包成執行檔。這樣一來，使用者就不需要安裝Python解釋器，只需執行生成的可執行檔即可運行程式。
在執行的路徑打上pyinstaller --onefile your_script_name.py，便可打包。

## Use
OpenCV
## 安裝所需套件
## Install
```sh
$ pip install opencv-python
```
```sh
$ pip install pyinstaller
```
```

