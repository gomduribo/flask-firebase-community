from flask import Flask, redirect, render_template, url_for, request
from DB_handler import DBModule

app = Flask(__name__)
DB = DBModule()

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/list")
def post_list():
    pass

@app.route("/post/<int>")
def post():
    pass

@app.route("/login")
def login():
    pass

@app.route("/login_done")
def login_done():
    pass

@app.route("/signin")
def signin():
    return render_template("signin.html")

# /signin_done으로 method가 들어올 거니까 get을 추가해주면 get을 받아올수 있다.
@app.route("/signin_done", methods= ["get"])
def signin_done():
    email = request.args.get("email")
    uid = request.args.get("id")
    pwd = request.args.get("pwd")
    name = request.args.get("name")
    
    if DB.signin(uid, pwd, name, email):
        return redirect(url_for("index"))
    else: 
        return redirect(url_for("signin"))

@app.route("/user/<uid>")
def user(uid):
    pass

@app.route("/write")
def write():
    pass

@app.route("/write_done", methods=["GET"])
def write_done():
    pass

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)