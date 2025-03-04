
from typing import *

from Block import Block





def do_it(data)->Block:
    #validating all the desired fields do exists
    needed_fields:List[str] = [
        "data",
        "index",
        "previous_hash",
        "pow",]
    for i in needed_fields:
        if i not in data:
            raise ValueError(f"[from_dict_block_maker]:field {i} is missing ")
        
    output:Block = Block(
        data=data["data"], 
        index=data["index"], 
        previous_hash=data["previous_hash"],
        pow=data["pow"],
        )
    
    return output