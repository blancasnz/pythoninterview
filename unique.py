

class Solution(object):

    def is_unique(self, input):
        if not input:
            return True

        characters = set()
        for char in input:
            lowercase = char.lower()
            if lowercase in characters:
                return False

            characters.add(lowercase)

        return True
