# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        prev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            third = slow.next
            slow.next = prev
            prev = slow
            slow = third
        if fast:
            slow = slow.next
        while prev and prev.val == slow.val:
            prev = prev.next
            slow = slow.next
        return not prev