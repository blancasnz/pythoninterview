
import unittest
from word_ladder import word_ladder


class WordLadderTest(unittest.TestCase):

    def test_word_ladder(self):
        start = 'hit'
        end = 'cog'
        words = ["hot", "dot", "dog", "lot", "log", "cog"]
        result = word_ladder(start, end, words)

        result_set = [set(r) for r in result]
        self.assertIn(set(["hit", "hot", "dot", "dog", "cog"]), result_set)
        self.assertIn(set(["hit", "hot", "lot", "log", "cog"]), result_set)

    def test_no_path(self):
        start = 'hit'
        end = 'cog'
        words = ["hot", "dot", "dog", "lot", "log"]
        result = word_ladder(start, end, words)

        self.assertFalse(result)
