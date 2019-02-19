# Remove all elements from a linked list of integers that have value val.
#
# Example:
#
# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head:
            if head.val==val:
                head=head.next
            else:
                break
        if not head:
            return None
        link=head
        while head.next:
            node=head.next
            if node.val==val:
                head.next=node.next
                continue
            head=head.next
        return link