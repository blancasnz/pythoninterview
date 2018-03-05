

class Solution(object):

    def letter_case_permutation(self, input):
        output = set()
        output.add(input)

        def permutate(prefix, suffix):
            if not suffix:
                output.add(prefix)
                return

            if suffix[0].isalpha():
                permutate(prefix + suffix[0].upper(), suffix[1:])
                permutate(prefix + suffix[0].lower(), suffix[1:])
            else:
                permutate(prefix + suffix[0], suffix[1:])

        permutate("", input)
        return output
