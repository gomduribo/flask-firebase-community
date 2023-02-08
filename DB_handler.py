import pyrebase
import json

class DBModule:
    def __init__(self):
        with open("./auth/firebaseAuth.json") as f:
            config = json.load(f)

        firebase = pyrebase.initialize_app(config)
        self.db = firebase.database()

    def login(self, uid, pwd): #데이터베이스에서 쓸것들 필요
        users = self.db.child("users").get().val()
        try:
            userinfo = users[uid]
            print(userinfo)
            if userinfo["password"] == pwd:
                return True
            else:
                return False
        except:
            return False

    def signin_verification(self, uid):
        users = self.db.child("users").get().val()
        for i in users:
            if uid == i:
                return False
        
        return True

    def signin(self, _id_, pwd, name, email):
        # print(f"id={_id_} pwd={pwd} name={name} email={email}")
        information = {
            "password": pwd,
            "name": name,
            "email": email
        }
        if self.signin_verification(_id_):
            self.db.child("users").child(_id_).set(information)
            return True
        else:
            return False

    def write_post(self, user, contents):
        pass

    def post_list(self):
        pass

    def post_detail(self, pid):
        pass

    def get_user(self, uid):
        pass
