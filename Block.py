from collections import OrderedDict
from typing import *
import hashlib

import dict_masher

class Block:
    def __init__(self, data:str, index:int, previous_hash:str, pow:str):
        self.data:str = data
        self.index = index 
        self.previous_hash = previous_hash
        self.pow = pow 

    def dictify(self)->Dict[str,Any]:
        output = OrderedDict()
        i:str #attr name
        for i in ["data", "index", "previous_hash", "pow"]:
            output[i] = getattr(self, i)
        return output
    
    def mash(self)->str:
        n:Dict[str,Any] = dict_masher.mash(self.dictify())
        return n

    def mash_without_pow(self)->str:
        n:Dict[str,Any] = dict_masher.mash(self.dictify())
        n.pop("pow")
        return n
    
    def hash_without_pow(self)->str:
        n:Dict[str,Any] = self.dictify()
        n.pop("pow")
        to_be_hashed:bytes = str(n).encode()
        hasher = hashlib.sha256()
        hasher.update(obj=to_be_hashed)
        return hasher.digest()
    
    def hash(self)->str:
        n:Dict[str,Any] = self.dictify()
        to_be_hashed:bytes = str(n).encode()
        hasher = hashlib.sha256()
        hasher.update(obj=to_be_hashed)
        return hasher.digest()  




    


