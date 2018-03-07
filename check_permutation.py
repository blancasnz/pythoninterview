
from collections import Counter


class Solution(object):

    def is_permutation(self, str1, str2):
        if len(str1) != len(str2):
            return False

        count = {}
        for index in range(len(str1)):
            char1 = str1[index].lower()
            char2 = str2[index].lower()

            count[char1] = count.get(char1, 0) + 1
            count[char2] = count.get(char2, 0) - 1

        return all([occurrence == 0 for occurrence in count.values()])
