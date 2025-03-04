
import binascii 



def do_it(data:bytes)->str:
    return (binascii.hexlify(data)).decode()



if __name__ == "__main__":
    print(
        do_it(b"abcdefgh")
    )

