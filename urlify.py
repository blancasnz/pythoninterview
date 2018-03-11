

class Solution(object):

    def urlify(self, input):
        output = []
        for char in input:
            if char == ' ':
                output.append('%20')
            else:
                output.append(char)

        return ''.join(output)
