from collections import OrderedDict
from typing import *
import hashlib

import dict_masher

import unhexlifier

import pow_validator

class Block:
    def __init__(self, data:str, index:int, previous_hash:str, pow:str):
        self.data:str = data
        self.index = index 
        self.previous_hash = previous_hash
        self.pow = pow 

    def dictify(self)->Dict[str,Any]:
        output = OrderedDict()
        i:str #attr name
        for i in ["data", "index",]:
            output[i] = getattr(self, i)
        output["previous_hash"] = unhexlifier.do_it(self.previous_hash)
        output["pow"] = unhexlifier.do_it(self.pow)
        return output
    
    def mash(self)->bytes:
        n:Dict[str,Any] = dict_masher.mash(self.dictify())
        return n.encode()

    def mash_without_pow(self)->bytes:
        n:Dict[str,Any] = dict_masher.mash(self.dictify())
        n.pop("pow")
        return n.encode()
    
    def hash_without_pow(self)->bytes:
        n:Dict[str,Any] = self.dictify()
        n.pop("pow")
        to_be_hashed:bytes = str(n).encode()
        hasher = hashlib.sha256()
        hasher.update(obj=to_be_hashed)
        return hasher.digest()
    
    def hash(self)->bytes:
        n:Dict[str,Any] = self.dictify()
        to_be_hashed:bytes = str(n).encode()
        hasher = hashlib.sha256()
        hasher.update(obj=to_be_hashed)
        return hasher.digest()  
    

    def is_valid(self)->bool:
        hashed:bytes = self.hash()
        return pow_validator.validate(hashed=hashed)




    


