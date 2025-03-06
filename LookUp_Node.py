
from flask import Flask, request

from LookUpRecord import LookUpRecord
from BaseNode import BaseNode 



class LookUp_Node(BaseNode):
    def __init__(self, ip, port, name):
        BaseNode.__init__(self, ip=ip, port=port, name=name)
        self.records:List[LookUpRecord] = list() 


    def get_record_by_name(self, name)->LookUpRecord:
        i:LookUpRecord 
        for i in self.records:
            if i.name == name:
                return i 
        return None
    

        


if __name__ == "__main__":
    pass