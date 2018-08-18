
def palindrome_list(head):
    values = []
    pointer = head
    while pointer:
        values.append(pointer.val)
        pointer = pointer.next
    return values == list(reversed(values))
