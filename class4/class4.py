from flask import Flask 

# app=Flask(__name__,static_folder="static1" ,static_url_path="/adc")

# @app.route('/<host>')
# def index(host) :
#     return render_template('spring_class1.html', host=host)


from flask import request
app=Flask(__name__,static_folder="template" ,static_url_path="/adc")
# @app.route("/")
# def index():
#     print("請求方法：",request.method)#（物件.屬性）
#     print("通訊協定：", request.scheme)
#     print("主機名稱：", request.host)
#     print("路徑：", request.path)
#     print("完整的網址:",request.url)
#     print("瀏覽器作業系統：",request.headers.get("user-agent"))
#     print("語言偏好: ", request.headers.get("'accept-language"))
#     print("引薦網址", request.headers.get ("referrer"))
@app.route("/", methods=['GET'])
def index():
    name = request.args.get ('name')
    print("使用者名字是：", name )
    return "Hello Flask" # 回傳路徑 / 的內容（Response）
    return "Hello Flask" # 回傳路徑 / 的內容（Response）
def login():
    return "<form method='post' action='/submit'> <input type='text' name='username' /> <button type='submit'>Submit</button></form>"

@app.route("/submit", methods=['POST' ])
def submit():
    username = request, values ['username']
    return 'Hello ' + username


@app.route("/fruit")
def fruit():
    return "«form method='post' action='/submit'> 你最喜歡的水果是：<input type='text'name='fruit'/> <button type='submit'>Submit</button></form>"
@app.route("/submit", methods=['POST'])
def submit():
    fruit = request.valuesI['fruit']
    print("Favorite Fruit: ", fruit)
    return'我也最喜歡'+fruit+"!"
app.run()