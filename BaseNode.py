
from flask import request, Flask 




class BaseNode:
    def __init__(self, ip:str, port:int, name:str):
        self.ip:str = ip 
        self.port:int = port 
        self.name:str = name
        self.app:Flask = Flask(name)
    

    def run(self):
        #plz run this in multithreaded manner
        self.app.run(host=self.ip, port=self.port, )


if __name__ == "__main__":
    b = BaseNode("0.0.0.0", 10000, "meow")
    b.run()