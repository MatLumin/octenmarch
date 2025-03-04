import binascii


def do_it(data:str)->bytes:
    return binascii.unhexlify(data.encode())


if __name__ == "__main__":
    pass