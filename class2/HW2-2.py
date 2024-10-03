from flask import Flask
app = Flask(__name__)# 建立 app 變數為 Flask 物件，__name_ 表示目前執行的程式capp.route（ "/"）# 使用函式裝飾器，建立一個路由（ Routes ），可針對主網域 / 發出請求def home （）： # 發出請求後會執行 home（）的函式
@app.route("/")# 使用函式裝飾器，建立一個路由（Routes ），可針對主網域 / 發出請求
def home():
    return"<h1>2024 Autumn</h1>" # 執行函式後會回傳特定的網頁內容，以HTML格式以方便瀏覽器來做網頁的展示發出請求後會執行 home（）的函式
app.run() # #*7