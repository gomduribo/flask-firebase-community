import pyrebase
import json

class DBModule:
    def __init__(self):
        with open("./auth/firebaseAuth.json") as f:
            config = json.load(f)

        self.firebase = pyrebase.initialize_app(config)

    def login(self, id, pwd): #데이터베이스에서 쓸것들 필요
        pass

    def signin(self, id, pwd, name, email):
        pass

    def write_post(self, user, contents):
        pass

    def post_list(self):
        pass

    def post_detail(self, pid):
        pass

    def get_user(self, uid):
        pass
