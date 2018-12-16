# Given two binary trees, write a function to check if they are the same or not.
#
# Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
#
# Example 1:
#
# Input:     1         1
#           / \       / \
#          2   3     2   3
#
#         [1,2,3],   [1,2,3]
#
# Output: true
# Example 2:
#
# Input:     1         1
#           /           \
#          2             2
#
#         [1,2],     [1,null,2]
#
# Output: false
# Example 3:
#
# Input:     1         1
#           / \       / \
#          2   1     1   2
#
#         [1,2,1],   [1,1,2]
#
# Output: false
class Solution(object):
    def isSameTree(self,p,q):
       """

       :param p:TreeNode
       :param q:TreeNode
       :return:bool
       """
       return self.isSameNode(p,q)
    def isSameNode(self,p,q):
        if p==None or q==None:
            if p==q: return True
            else: return False

        else:
            if p.val!=q.val: return False
            else:
                l=self.isSameNode(p.left,q.left)
                r=self.isSameNode(p.right,q.right)
                if l==True and r==True: return True
                else: return False



