from typing import *

from flask import Flask, request, render_template

from LookUpRecord import LookUpRecord
from BaseNode import BaseNode 
import CONSTANT


STANDARD_OUTPUT = {
    "is_ok":False,
    "data":None,
    "error_msg":None,
    }

class LookUp_Node(BaseNode):
    def __init__(self):
        BaseNode.__init__(self, ip=CONSTANT.LOOOK_UP_NODE_IP, port=CONSTANT.LOOK_UP_NODE_PORT, name="LOOK_UP_NODE", type="LOOKUP")
        self.records:List[LookUpRecord] = list() 
        self.record_dump:List[LookUp_Node] = list() #we put dead and offlien nodes here


        @self.app.get("/gui/info")
        def gui_info():
            return render_template("lookup_node/info.html", lookupnode=self)


        @self.app.post("/api/holder_nodes_count")
        def api_holder_nodes_count():
            count:int 
            for i in self.records:
                if i.type == "HOLDER":
                    count += 1
            return {
                "is_ok":True, 
                "data":count #assuming dead notes are removed before
                }


        @self.app.post("/api/express")
        def api_express():
            
            posted_data:Dict[str,Any] = request.json
            if "ip" not in posted_data:
                o = STANDARD_OUTPUT.copy()
                o["error_msg"] = "ip is missing from fields"
                return o
            if "port" not in posted_data:
                o = STANDARD_OUTPUT.copy()
                o["error_msg"] = "port is missing from fields"
                return o
            if "name" not in posted_data:
                o = STANDARD_OUTPUT.copy()
                o["error_msg"] = "name is missing from fields"
                return o
            if "type" not in posted_data:
                o = STANDARD_OUTPUT.copy()
                o["error_msg"] = "type is missing from fields"
                return o    

            ip = request.json["ip"]
            port = request.json["port"]
            name = request.json["name"]
            _type:str = request.json["type"]
            
            if isinstance(port, int) == False:
                o = STANDARD_OUTPUT.copy()
                o["error_msg"] = "port must be a number"
                return o  
            
            if (0 <= port <= 65535) == False:
                o = STANDARD_OUTPUT.copy()
                o["error_msg"] = "port must be in valid range"
                return o       



            query_of_ip:List[LookUpRecord] = self.query_records(ip=ip)
            query_of_port:List[LookUpRecord] = self.query_records(port=port)
            query_of_name:List[LookUpRecord] = self.query_records(name=name)
            print("[query_of_ip]", query_of_ip)
            print("[query_of_port]", query_of_port)
            print("[query_of_name]", query_of_name)

            #if query_of_ip.__len__() != 0:
                #o = STANDARD_OUTPUT.copy()
                #o["error_msg"] = "ip is already occupied"
                #return o
            if query_of_port.__len__() != 0:
                o = STANDARD_OUTPUT.copy()
                o["error_msg"] = "port is already occupied"
                return o
            if query_of_name.__len__() != 0:
                o = STANDARD_OUTPUT.copy()
                o["error_msg"] = "name is already occupied"
                return o 

            r:LookUpRecord = LookUpRecord(
                ip=ip,
                port=port, 
                name=name,
                type=_type
                )
            self.records.append(r)
            o = STANDARD_OUTPUT.copy()
            o["is_ok"] = True 
            return o
        

        @self.app.route("/api/get_node_record")
        def api_get_node_record():
            if "name" not in request.json:
                o = STANDARD_OUTPUT.copy()
                o["error_msg"] = "NAME_MISSING"
                return o

            name:str = request.json["name"]
            query_result:List[LookUpRecord] = self.get_record_by_name(name=name)
            if len(query_result) == 0:
                o = STANDARD_OUTPUT.copy()
                o["error_msg"] = "NOT_FOUND"
                return o 
            

            o = STANDARD_OUTPUT.copy()
            o["is_ok"] = True
            o["data"] = query_result[0].dictify()
            return o


    def get_record_by_name(self, name)->LookUpRecord:
        i:LookUpRecord 
        for i in self.records:
            if i.name == name:
                return i 
        return None
    
    def query_records(self, **kwargs)->List[LookUpRecord]:
        output:List[LookUpRecord] = []
        for i in self.records:
            piko:bool = True 
            for attrname, desiredvalue in kwargs.items():
                piko &= getattr(self, attrname, None) == desiredvalue
                output.append(i)
        return output
    

    def clear_offline_node_records():
        pass
    

    def run(self):
        BaseNode.run(self)
    


    

        


if __name__ == "__main__":
    pass