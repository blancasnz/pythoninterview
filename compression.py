

class Solution(object):

    def compress(self, input):
        if not input:
            return ''

        output = []

        count = 0
        current = input[0]
        for i in range(len(input)):
            if input[i] == current:
                count += 1

            if input[i] != current or i == len(input) - 1:
                output.append(current)
                if count > 1:
                    output.append(str(count))
                count = 1
                current = input[i]

        return ''.join(output)
