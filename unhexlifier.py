import binascii


def do_it(data:bytes)->bytes:
    return binascii.unhexlify(data)


if __name__ == "__main__":
    pass