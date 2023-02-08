from flask import Flask, redirect, render_template, url_for, request, session, flash
from DB_handler import DBModule

app = Flask(__name__)
app.secret_key = "dkdkdkdkdkd"
DB = DBModule()

@app.route("/")
def index():
    if "uid" in session:
        user = session["uid"]
    else:
        user = "Login"
    return render_template("index.html", user=user)


@app.route("/list")
def post_list():
    pass

@app.route("/post/<int>")
def post():
    pass

@app.route("/logout")
def logout():
    if "uid" in session:
        session.pop("uid")
        return redirect(url_for("index"))
    else:
        return redirect(url_for("login"))

@app.route("/login")
def login():
    if "uid" in session:
        return redirect(url_for("index"))
    return render_template("login.html")

@app.route("/login_done", methods= ["get"])
def login_done():
    uid = request.args.get("id")
    pwd = request.args.get("pwd")
    if DB.login(uid, pwd):
        session["uid"] = uid
        return redirect(url_for("index"))
    else:
        flash("아이디가 없가나 비밀번호가 틀립니다.")
        return redirect(url_for("login"))
    return "None"

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
        flash("이미 존재하는 아이디입니다.")
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