from typing import *
from Block import Block 

import mash_and_pow_combiner


def mine(mashed:str)->str:
    #mashed is the decoded hexlified 
    raw_pow:int = 0
    while True:
        combined:str = mash_and_pow_combiner.combine(mash=mashed)
