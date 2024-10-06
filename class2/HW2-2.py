# from flask import Flask
# app = Flask(__name__)# 建立 app 變數為 Flask 物件，__name_ 表示目前執行的程式capp.route（ "/"）# 使用函式裝飾器，建立一個路由（ Routes ），可針對主網域 / 發出請求def home （）： # 發出請求後會執行 home（）的函式
# @app.route("/")# 使用函式裝飾器，建立一個路由（Routes ），可針對主網域 / 發出請求
# def home():
#     return"<h1>2024 Autumn</h1>\<h2>學習flask<h2>" # 執行函式後會回傳特定的網頁內容，以HTML格式以方便瀏覽器來做網頁的展示發出請求後會執行 home（）的函式
# app.run()
# @app. route("/user/<name>")
# def getUser (name):
#     return "Hello "+name

# from flask import Flask 
# app=Flask(__name__)
# @app.route("/")
# def index():
#     return "Welcome to my Web!"
# @app. route("/member/<name>")
# def sayHi (name):
#     return "Hello, our favorite member: "+name
# @app. route("/admia/<level>")
# def login (level):
#     if level=="A":
#         return "Login here!"
#     else:
#         return "You can not login in!"

# app.run()



from flask import Flask 

app=Flask(__name__,static_folder="static" ,static_url_path="/adc")
@app.route("/")
def index():
    return "Welcome to my Web!"
app.run()