from typing import *
import unittest

import hexlifier
import unhexlifier
import from_dict_block_maker
from Block import Block


class HexThings(unittest.TestCase):
    def test_1(self):
        test_text:bytes = b"HELLO WORLD"
        resulted_text:bytes = unhexlifier.do_it(hexlifier.do_it(test_text))
        result:bool = resulted_text == test_text
        self.assertTrue(result)


class BlockEncodingAndDecodingIntegrity(unittest.TestCase):
    def test_1(self):
        block = Block(
            data="hello world",
            index=0,
            previous_hash=b"pewpew",
            pow=b"piko[ikp]"
        )

        as_dict:Dict[str,Any] = block.dictify()

        reformed:Block = from_dict_block_maker.form(as_dict)

        print("[formed]", reformed)
        print("[block]", block)

        result:bool = reformed == block
        self.assertTrue(result)
