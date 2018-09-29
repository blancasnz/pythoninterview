from collections import deque


class NestedInteger(object):
    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """


class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.queue = deque(self.flatten(nestedList))

    def flatten(self, nested_list):
        if not nested_list:
            return []

        output = []
        for item in nested_list:
            if item.isInteger():
                output.append(item)
            else:
                output.extend(self.flatten(item.getList()))
        return output

    def next(self):
        """
        :rtype: int
        """
        popped = self.queue.popleft()
        return popped.getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.queue) > 0
