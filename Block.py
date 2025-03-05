from collections import OrderedDict
from typing import *
import hashlib

import dict_masher

import unhexlifier
import hexlifier

import pow_validator

class Block:
    def __init__(self, data:str, index:int, previous_hash:bytes, pow:bytes):
        self.data:str = data
        self.index:int = index 
        self.previous_hash:bytes = previous_hash
        self.pow:bytes = pow 

    def __eq__(self, other)->bool:
        output:bool = True
        output &= self.data == other.data
        output &= self.index == other.index
        output &= self.previous_hash == other.previous_hash
        output &= self.pow == other.pow
        return output
    
    def __str__(self)->str:
        return f"<Block d:{self.data} i:{self.index} ph:{self.previous_hash} pow:{self.previous_hash}"
    
    def __repr__(self):return str(self)

    def dictify(self)->Dict[str,Any]:
        output = OrderedDict()
        i:str #attr name
        for i in ["data", "index",]:
            output[i] = getattr(self, i)
        output["previous_hash"] = hexlifier.do_it(self.previous_hash)
        output["pow"] = hexlifier.do_it(self.pow)
        print("[dictify]", output)
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




    


