# Write a program to find the node at which the intersection of two singly linked lists begins.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        hashset = {}
        while headA:
            hashset[headA] = None
            headA = headA.next
        while headB:
            if headB in hashset:
                return headB
            headB = headB.next
        return None

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1=headA
        p2=headB
        AlastNode=None
        BlastNode=None
        while p1 and p2:
            if p1==p2 and (p1 or p2):
                return p1
            if not p1.next:
                AlastNode=p1
                p1=headB
            else :
                p1=p1.next
            if not p2.next:
                BlastNode=p2
                p2=headA
            else:
                p2=p2.next
            if AlastNode and BlastNode and (AlastNode is not BlastNode):
                return None