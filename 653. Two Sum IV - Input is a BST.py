# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """

        Set = set()
        return self.find(root, k, Set)

    def find(self, node, k, Set):
        if not node:
            return False
        if (k - node.val) in Set:
            return True
        Set.add(node.val)
        return self.find(node.left, k, Set) or self.find(node.right, k, Set)

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        Set=set()
        stack=[]
        if root:
            stack.append(root)
        while stack:
            node=stack.pop()
            if node:
                if (k-node.val) in Set:
                    return True
                else:
                    Set.add(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return False