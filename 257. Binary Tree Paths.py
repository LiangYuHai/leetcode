# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        res=[]
        self.buildpath(root,res,'')
        return res
    def buildpath(self,node,res,path):
        if not node.left and not node.right:
            res.append(path+str(node.val))
        if node.left:
            self.buildpath(node.left,res,path+str(node.val)+'->')
        if node.right:
            self.buildpath(node.right,res,path+str(node.val)+'->')

from collections import deque
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        queue=deque([(root,str(root.val)+'->')])
        res=[]
        while queue:
            node=queue.popleft()
            if not node[0].left and not node[0].right:
                res.append(node[1][:-2])
            if node[0].left:
                queue.append((node[0].left,node[1]+str(node[0].left.val)+'->'))
            if node[0].right:
                queue.append((node[0].right,node[1]+str(node[0].right.val)+'->'))
        return res

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        stack=[(root,str(root.val)+'->')]
        res=[]
        while stack:
            node=stack.pop()
            if not node[0].left and not node[0].right:
                res.append(node[1][:-2])
            if node[0].right:
                stack.append((node[0].right,node[1]+str(node[0].right.val)+'->'))
            if node[0].left:
                stack.append((node[0].left,node[1]+str(node[0].left.val)+'->'))
        return res