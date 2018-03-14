import unittest

from remove_dup_linked_list import remove_dup
from list_node import ListNode


class RemoveDuplicatesTests(unittest.TestCase):

    def test_remove_dup(self):
        self.assertEqual(
            remove_dup(ListNode.from_list([1, 1, 1])),
            ListNode.from_list([1])
        )

        self.assertEqual(
            remove_dup(ListNode.from_list([1])),
            ListNode.from_list([1])
        )

        self.assertEqual(
            remove_dup(ListNode.from_list([1, 2, 3, 3])),
            ListNode.from_list([1, 2, 3])
        )

        self.assertEqual(
            remove_dup(ListNode.from_list([1, 2, 2, 3])),
            ListNode.from_list([1, 2, 3])
        )
