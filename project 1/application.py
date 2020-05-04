from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("layout.html")

texts = ["WELCOME to HomePage","Service Page","About us page","Contact page"]

@app.route("/home")
def home():
    return texts[0]


@app.route("/service")
def service():
    return texts[1]




@app.route("/about")
def about():
    return texts[2]




@app.route("/contact")
def contact():
    return texts[3]




