

def strstr(haystack, needle):
    for index_a in range(len(haystack)):
        for index_b in range(len(needle)):
            if (
                index_a + index_b >= len(haystack) or
                haystack[index_a + index_b] != needle[index_b]
            ):
                break

            if index_b == len(needle) - 1:
                return index_a

        return -1
