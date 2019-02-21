class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        e = self.stack[0]
        del self.stack[0]
        return e

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.stack[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.stack == []