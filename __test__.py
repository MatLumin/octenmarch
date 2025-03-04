import unittest

import hexlifier
import unhexlifier


class HexThings(unittest.TestCase):
    def test_1(self):
        test_text:bytes = b"HELLO WORLD"
        resulted_text:bytes = unhexlifier.do_it(hexlifier.do_it(test_text))
        result:bool = resulted_text == test_text
        self.assertTrue(result)


class HexThings(unittest.TestCase):
    def test_1(self):
        test_text:bytes = b"HELLO WORLD"
        resulted_text:bytes = unhexlifier.do_it(hexlifier.do_it(test_text))
        result:bool = resulted_text == test_text
        self.assertTrue(result)