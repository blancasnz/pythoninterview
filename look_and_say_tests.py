import unittest

from look_and_say import look_and_say


class LookAndSayTests(unittest.TestCase):

    def test_10(self):
        expected = [
            '1',
            '11',
            '21',
            '1211',
            '111221',
            '312211',
            '13112221',
            '1113213211',
            '31131211131221',
            '13211311123113112211',
        ]
        self.assertEqual(look_and_say(10), expected)
