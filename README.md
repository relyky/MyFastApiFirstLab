# My FastApi first 
* FastAPI WebApi/Swagger 網站試作。
* 因為它是用 Python 程式語言實作的網站。
* 為了評估是否引用此技術。

# 開發環境
1. Python v3.11
2. IDE: Visual Studio Code
3. [Uvicorn](https://www.uvicorn.org/) is an ASGI web server implementation for Python. 
4. [FastAPI](https://fastapi.tiangolo.com/) is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.

# 參考文件
* [FastAPI](https://fastapi.tiangolo.com/)
* [Uvicorn](https://www.uvicorn.org/)
* [Fast API Tutorial, Part 1: Introduction](https://www.youtube.com/watch?v=XnYYwcOfcn8&list=PLqAmigZvYxIL9dnYeZEhMoHcoP4zop8-p&ab_channel=JVPDesign)
* [Python FastAPI 快速(指令)入門](https://linyencheng.github.io/2021/10/08/python-fast-api/)   

# 關於部署(備用)
依照 [Uvicorn - Deployment](https://www.uvicorn.org/deployment/) 部署說明可以部署到數個環境，但我們優先希望部署到 IIS 次為 Windows Services。
### 部署到 IIS
* [Configure Python web apps for IIS](https://learn.microsoft.com/en-us/visualstudio/python/configure-web-apps-for-iis-windows?view=vs-2022)
* [How to deploy a FastAPI web app on IIS server?](https://stackoverflow.com/questions/68664339/how-to-deploy-a-fastapi-web-app-on-iis-server)
### 部署成 Windows Service 
* [Windows Service in Python](https://github.com/kbeaugrand-org/PythonFastApi)
* [FastAPI as a Windows service](https://stackoverflow.com/questions/65591630/fastapi-as-a-windows-service)
* [How to Create a FastAPI / Uvicorn Server Windows Service](https://medium.com/codex/how-to-create-a-fastapi-uvicorn-server-windows-service-af41f075dabf)
* [PyInstaller](https://pyinstaller.org/)

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
uvicorn main:app --reload --port 8000
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
成功的話就能：
1) 在網址：`http://127.0.0.1:8000/` 看到東西。   
2) 在網址：`http://127.0.0.1:8000/docs` 在看到 swagger 文件。    
   
![圖一](https://github.com/relyky/MyFastApiFirstLab/blob/main/doc/%E5%9C%96%E7%89%87%20001.png)
![圖二](https://github.com/relyky/MyFastApiFirstLab/blob/main/doc/%E5%9C%96%E7%89%87%20002.png)

加入新的API，此例為`book/{book_id}`，swagger 文件也相應更新。   
   
![圖三](https://github.com/relyky/MyFastApiFirstLab/blob/main/doc/%E5%9C%96%E7%89%87%20003.png)
![圖四](https://github.com/relyky/MyFastApiFirstLab/blob/main/doc/%E5%9C%96%E7%89%87%20004.png)
