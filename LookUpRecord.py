from typing import * 

import requests


class LookUpRecord:
    def __init__(self, ip:str, port:int, name:str, type:str):
        self.ip:str = ip
        self.port:int = port
        self.name:str = name
        self.type = type

    def is_online(self)->bool:
        try:
            requests.get(
            url=f"http://{self.ip}:{self.port}/is_online"
            )
        except requests.Timeout:
            return False
        return True
    
    def dictify(self)->Dict[str,Any]:
        return {
            "ip":self.ip,
            "port":self.port,
            "name":self.name,
            "type":self.type,
        }

    def __str__(self):
        return f"<LooKUpRecord {self.ip}:{self.port};{self.name};{self.type}>"
    
    def __repr__(self):return str(self)