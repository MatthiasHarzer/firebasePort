import os, subprocess, sys, pyrebase
class Database(object):
    def __init__(self):
        config = {
            "apiKey": "APIKEY",
            "authDomain": "AUTHDOMAI ",
            "databaseURL": "URL",
            "storageBucket": "STORAGEBUCKET",
            "tls": {
                "rejectUnauthorized": False
                }
            }
        self.firebase = pyrebase.initialize_app(config)
        self.db = self.firebase.database()
        
    def writeData(self, path, data):
        path = path.split('/')
        for i in path:
            self.db = self.db.child(i)
        self.db.set(data)
        
