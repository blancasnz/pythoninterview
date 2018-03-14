
class ListNode(object):

    def __init__(self, val):
        self.val = val
        self.next = None

    @classmethod
    def from_list(cls, values):
        head = None
        for val in reversed(values):
            entry = cls(val)
            entry.next = head
            head = entry
        return head

    def __eq__(self, other):
        if not other or self.val != other.val:
            return False

        return self.next == other.next

    def __repr__(self):
        return f'<ListNode {self.val}>'
