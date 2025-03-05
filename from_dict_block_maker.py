
from typing import *

from Block import Block
import unhexlifier




def form(data:Dict[str,Any])->Block:
    #validating all the desired fields do exists
    needed_fields:List[str] = [
        "data",
        "index",
        "previous_hash",
        "pow",]
    for i in needed_fields:
        if i not in data:
            raise ValueError(f"[from_dict_block_maker]:field {i} is missing ")
        
    pow_raw:str = data["pow"] #hexlified version 
    pow_processed:bytes = unhexlifier.do_it(data=pow_raw)
    previous_hash_raw:str = data["previous_hash"] #hexlified version 
    previous_hash_processed:bytes = unhexlifier.do_it(data=previous_hash_raw)
    output:Block = Block(
         
        data=data["data"], 
        index=data["index"], 
        previous_hash=previous_hash_processed,
        pow=pow_processed,
        )
    
    return output