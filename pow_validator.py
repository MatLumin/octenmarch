


import mash_and_pow_combiner 





def validate(hashed:str)->bool:
    #hashed is decoded hexlified 
    return hashed.count("a") > 8