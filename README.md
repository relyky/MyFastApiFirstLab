# My FastApi first 
* FastAPI WebApi/Swagger 網站試作。
* 因為它是用 Python 程式語言實作的網站。
* 為了評估是否引用此技術。

# 開發環境
1. Python v3.11
2. IDE: Visual Studio Code

# 參考文件
* [FastAPI](https://fastapi.tiangolo.com/)
* [Fast API Tutorial, Part 1: Introduction](https://www.youtube.com/watch?v=XnYYwcOfcn8&list=PLqAmigZvYxIL9dnYeZEhMoHcoP4zop8-p&ab_channel=JVPDesign)
* [Python FastAPI 快速(指令)入門](https://linyencheng.github.io/2021/10/08/python-fast-api/)   

# 開發時下達指令主要過程
---------------------------
```
python -V                              # 檢查 Python 版本

python -m venv env                     # 建立 Python 執行虛擬環境

.\env\Scripts\activate                 # 切入 Python 虛擬空間

...[requirements.txt]...               # 編輯需要的相依套件

python -m pip install --upgrade pip    # 可能需先更新 pip 版本。
pip install -r .\requirements.txt      # 安裝需要的相依套件,依據 requirements.txt 套件需求清單來安裝。(有點像 npm 的 package.json 檔)

...[main.py]...                        # 開發 Web Api 進入點。一般進入檔名叫 main.py ；進入物件叫 app。

uvicorn main:app                       # 啟動 Web API 並產生 Swagger 文件。
# 其中 "mian:app" 是指：
# (1)使用 main.py 檔建立 WebApi。
# (2)啟動物件名稱為 app。
```
---------------------------
# 結論
* 可以快速做出 Web API 並產生 Swagger 文件。
* 其實就是 Python 版的 MiniAPI。
* 其它安全性等等的部份要再一一加入。

# 沒圖沒真象
