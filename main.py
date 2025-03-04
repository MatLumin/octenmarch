
from typing import * 

from flask import Flask

from Block import Block




blockchain:List[Block] = list()

app:Flask = Flask("yippe")



@app.get("/ui/config")
def ui_config():
    pass




