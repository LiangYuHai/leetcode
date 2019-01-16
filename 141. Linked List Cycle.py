# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        checknode = ListNode(0)
        if not head:
            return False
        node = head
        while node.next:
            if node.next == checknode:
                return True
            checked = node
            node = node.next
            checked.next = checknode

        return False
#hash
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False

        nodeScan = {}

        while head:
            if head in nodeScan:
                return True
            else:
                nodeScan[head] = None
                head = head.next

        return False
#two runner
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        slow=head
        fast=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False