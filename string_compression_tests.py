import unittest

from string_compression import compress


class StringCompressionTests(unittest.TestCase):

    def test_string_compression(self):
        self.assertEquals(compress('aabccdddde'), 'aabccdddde')
        self.assertEquals(compress('aabccddddD'), 'a2b1c2d5')
        self.assertEquals(compress('aaaabbbaaa'), 'a4b3a3')
        self.assertEquals(compress('a'), 'a')
        self.assertEquals(compress('AAAaaa'), 'a6')
        self.assertEquals(compress(None), None)
        self.assertEquals(compress(''), '')
