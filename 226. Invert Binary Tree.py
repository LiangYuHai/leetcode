class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        DFS=[root]
        while DFS:
            node=DFS.pop()
            if node:
                node.left,node.right=node.right,node.left
                DFS.append(node.right)
                DFS.append(node.left)
        return root

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        BFS=collections.deque([root])
        while BFS:
            node=BFS.popleft()
            if node:
                node.left,node.right=node.right,node.left
                BFS.append(node.left)
                BFS.append(node.right)
        return root
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            root.left,root.right=self.invertTree(root.right),self.invertTree(root.left)
            return root