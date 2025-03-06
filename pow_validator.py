







def validate(hashed:bytes)->bool:
    #hashed is decoded hexlified 
    return hashed.count(b"0") > 3