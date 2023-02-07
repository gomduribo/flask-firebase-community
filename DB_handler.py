import pyrebase
import json

class DBModule:
    def __init__(self):
        with open("./auth/firebaseAuth.json") as f:
            config = json.load(f)

        firebase = pyrebase.initialize_app(config)
        self.db = firebase.database()

    def login(self, id, pwd): #데이터베이스에서 쓸것들 필요
        pass

    def signin(self, _id_, pwd, name, email):
        # print(f"id={_id_} pwd={pwd} name={name} email={email}")
        information = {
            "password": pwd,
            "name": name,
            "email": email
        }
        self.db.child("users").child(_id_).set(information)

    def write_post(self, user, contents):
        pass

    def post_list(self):
        pass

    def post_detail(self, pid):
        pass

    def get_user(self, uid):
        pass
