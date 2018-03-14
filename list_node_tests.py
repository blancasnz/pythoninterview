import unittest

from list_node import ListNode


class ListNodeTests(unittest.TestCase):

    def test_equality(self):
        l1 = ListNode(1)
        l2 = ListNode(1)

        self.assertEqual(l1, l2)

        l1.next = ListNode(2)
        l2.next = ListNode(2)
        self.assertEqual(l1, l2)

        l1.val = 3
        self.assertNotEqual(l1, l2)

    def test_from_list(self):
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(3)
        node1.next = node2
        node2.next = node3
        node3.next = node4

        self.assertEqual(node1, ListNode.from_list([1, 2, 3, 3]))
