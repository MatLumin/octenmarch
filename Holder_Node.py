from typing import *
import ipaddress

from Block import Block
from BaseNode import BaseNode
import requests
import CONSTANT


class Holder_Node(BaseNode):
    def __init__(self, ip, port, name,):
        BaseNode.__init__(self, ip=ip, port=port, name=name, type="HOLDER")

    







        