from flask import Flask 

app=Flask(__name__,static_folder="static1" ,static_url_path="/adc")
@app.route("/")
def index():
    return "Welcome to my Web!"
app.run()
