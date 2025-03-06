import time

from Block import Block
import pow_validator




def mine(z:Block)->bytes:
    pow:int = 0
    while True:
        pow_as_bytes:bytes = str(pow).encode()
        hashed:bytes = z.hash_by_pow(pow=pow_as_bytes)
        if pow_validator.validate(hashed=hashed):
            break 
        pow += 1
    print(pow)
    return pow




if __name__ == "__main__":
    z:Block = Block(
        data="Hello world and some more fact on the block chain",
        index=0,
        previous_hash=b"0",
        pow=b""
    )
    mine(z)