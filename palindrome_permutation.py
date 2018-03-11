from collections import Counter


class Solution(object):

    def palindrome_permutation(self, input):
        counter = Counter(input.lower())
        filtered = [k for k, v in counter.items() if v % 2 == 1 and k != ' ']
        return len(filtered) <= 1
