# iven a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
# But the following [1,2,2,null,3,null,3] is not:
#     1
#    / \
#   2   2
#    \   \
#    3    3
# Note:
# Bonus points if you could solve it both recursively and iteratively.
class solution1:#recursive
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None: return True
        return self.isMirror(root.left,root.right)

    def isMirror(self,t1,t2):
        if t1 is None and t2 is None: return True
        elif t1 is None or t2 is None: return False
        else:
            if t1.val!=t2.val: return False
            else:
                return (self.isMirror(t1.left,t2.right) and self.isMirror(t1.right,t2.left))

class solution2:#iterative
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None: return True
        q = []
        q.append(root.left)
        q.append(root.right)
        while q:
            t1 = q.pop()
            t2 = q.pop()
            if t1 is None and t2 is None: continue
            if t1 is None or t2 is None: return False
            if t1.val != t2.val:
                return False
            q.append(t1.left)
            q.append(t2.right)
            q.append(t1.right)
            q.append(t2.left)
        return True

