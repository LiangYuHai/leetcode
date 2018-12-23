# Given a binary tree, determine if it is height-balanced.
#
# For this problem, a height-balanced binary tree is defined as:
#
# a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
#
# Example 1:
#
# Given the following tree [3,9,20,null,null,15,7]:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Return true.
#
# Example 2:
#
# Given the following tree [1,2,2,3,3,null,null,4,4]:
#
#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
# Return false.
#O(n!)
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        else:
            deepleft = self.maxDepth(root.left)
            deepright = self.maxDepth(root.right)
        if abs(deepleft - deepright):
            if self.isBalanced(root.left) and self.isBalanced(root.right):
                return True
            else:
                return False
        else:
            return False

    def maxDepth(self, node):
        if node:
            return 1 + max(self.maxDepth(node.left), self.maxDepth(node.right))
        else:
            return 0

# O(n)
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if self.isBalancedHelp(root) == -1:
            return False
        else:
            return True

    def isBalancedHelp(self, root):
        if not root:
            return 0
        l = self.isBalancedHelp(root.left)
        r = self.isBalancedHelp(root.right)

        if l != -1 and r != -1:
            if abs(l - r) > 1:
                return -1
            else:
                return 1 + max(l, r)
        return -1