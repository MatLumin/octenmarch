from typing import *
import ipaddress

from Block import Block
from BaseNode import BaseNode


class Holder_Node(BaseNode):
    def __init__(self, ip, port, name):
        BaseNode.__init__(self, ip=ip, port=port, name=name)
        self.look_up_node_ip = None 
        self.look_up_node_port = None




        