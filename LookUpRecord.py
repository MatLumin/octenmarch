import requests


class LookUpRecord:
    def __init__(self, ip:str, port:int, name:str):
        self.ip:str = ip
        self.port:int = port
        self.name:str = username

    def is_online(self)->bool:
        try:
            requests.get(
            url=f"http://{self.ip}:{self.port}/is_online"
            )
        except requests.Timeout:
            return False
        return True

    def __str__(self):
        return f"<LoopUpRecord {self.ip}:{self.port} ; {self.name}>"
    
    def __repr__(self):return str(self)