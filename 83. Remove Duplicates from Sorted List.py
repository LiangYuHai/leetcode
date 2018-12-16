# Given a sorted linked list, delete all duplicates such that each element appear only once.
# #
# # Example 1:
# #
# # Input: 1->1->2
# # Output: 1->2
# # Example 2:
# #
# # Input: 1->1->2->3->3
# # Output: 1->2->3
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution1(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None: return None
        p1=head
        p2=head.next
        while p2:
            if p2.val==p1.val:
                p1.next=p2.next
            else:
                p1=p1.next
            p2=p2.next
        return head

class Solution2(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        removed_list=ListNode(0)
        Head=removed_list
        removed_list.next=head
        removed_list=removed_list.next
        while head.next:
            head=head.next
            if removed_list.val==head.val:
                continue
            else:
                removed_list.next=head
                removed_list=removed_list.next
        if head.val==removed_list.val: removed_list.next=None
        return Head.next