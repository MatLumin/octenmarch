from threading import Thread
import time 


import requests
from flask import request, Flask 

import CONSTANT




class BaseNode:
    def __init__(self, ip:str, port:int, name:str, type="BASE"):
        self.ip:str = ip 
        self.port:int = port 
        self.name:str = name
        self.type:str = type
        self.app:Flask = Flask(name)

        @self.app.route("/is_online")
        def is_online():
            return {"is_ok":True, "data":True}
    

    def run(self):
        #plz run this in multithreaded manner
        def f():
            self.app.run(host=self.ip, port=self.port, )

        def g():
            time.sleep(3)
            while True:
                self.express_to_look_up_node()
                time.sleep(60.0)
            
            
        flask_thread:Thread = Thread(target=f)
        expressor_thread:Thread = Thread(target=g)

        flask_thread.start()
        expressor_thread.start()

        flask_thread.join()
        expressor_thread.join()

    def express_to_look_up_node(self):
        try:
            requests.post(
                url=F"http://{CONSTANT.LOOOK_UP_NODE_IP}:{CONSTANT.LOOK_UP_NODE_PORT}/api/express",
                json={"ip":self.ip, "port":self.port, "name":self.name, "type":self.type}
                )
        except requests.exceptions.ConnectionError:
            return None



        


if __name__ == "__main__":
    b = BaseNode("0.0.0.0", 10000, "meow")
    b.run()

