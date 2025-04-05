from typing import * 

import requests


import CONSTANT



def get_record_by_name()->Dict[str, Any]:
    #returns None on time out Error
    try:
        req:requests.Request = requests.get(f"http://{CONSTANT.LOOOK_UP_NODE_IP}/{CONSTANT.LOOK_UP_NODE_PORT}/api/holder_nodes_count")
        return req.json["data"]
    except TimeoutError:
        return None


def get_holder_node_count()->int:
    try:
        req:requests.Request = requests.get(f"http://{CONSTANT.LOOOK_UP_NODE_IP}/{CONSTANT.LOOK_UP_NODE_PORT}/api/holder_nodes_count")
        return req.json["data"]
    except TimeoutError:
        return 0