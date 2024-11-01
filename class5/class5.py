from flask import Flask, render_template, request
import json
from flask import Flask, url_for, redirect
app = Flask(__name__)



@app. route('/response') 
def example_response ():
    lang = request.headers.get ("accept_language")
    if lang.startswith("zh" ) :
        return json.dumps({"text": "你好"}, ensure_ascii=False)
    else:
        return json.dumps({"text": "Hello"}, ensure_ascii=False)
app.run()


@app. route("/hello")
def say_hi():
    session=()
    name = request.args.get ("name","")
    session['username'] = name
#將 GET 中得到的 Query String儲存到 Session 中
    return "Hi, "+name
@app. route("/talk")
def talk():
    name = session ['username']
    return "Long time no see~"+name

@app. route("/github" )
def github():
    return "<form method='post' action='/submit'> <input type='text' name='username' /> <button type='submit'>Submit</button></form>"
@app.route("/submit", methods=['POST'])
def go_github () :
    username = request. values ['username' ]
    return redirect("https://github.com/"+username)