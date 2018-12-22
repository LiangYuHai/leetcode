# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None: return []
        if root:
            res = []
            res.append([root.val])
            node = []
            node.append(root)

        while node:
            tempnode = []
            tempval = []
            for i in node:
                if i.left:
                    tempnode.append(i.left)
                    tempval.append(i.left.val)
                if i.right:
                    tempnode.append(i.right)
                    tempval.append(i.right.val)
            if tempval:
                res.append(tempval)
            node = tempnode

        return res[::-1]