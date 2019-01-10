# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Iteration DFS
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        children = [root.left, root.right]
        if not any(children):
            return 1

        min_depth = float('inf')
        for c in children:
            if c:
                min_depth = min(self.minDepth(c), min_depth)
        return min_depth + 1

# Approach 2: DFS Iteration
# We could also convert the above recursion into iteration, with the help of stack.
# The idea is to visit each leaf with the DFS strategy, while updating the minimum depth when we reach the leaf node.
# So we start from a stack which contains the root node and the corresponding depth which is 1. Then we proceed to the
# iterations: pop the current node out of the stack and push the child nodes. The minimum depth is updated at each leaf node.
class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            stack, min_depth = [(1, root), ], float('inf')

        while stack:
            depth, root = stack.pop()
            children = [root.left, root.right]
            if not any(children):
                min_depth = min(depth, min_depth)
            for c in children:
                if c:
                    stack.append((depth + 1, c))
        return min_depth



# Approach 3: BFS Iteration
# The drawback of the DFS approach in this case is that all nodes should be visited to ensure t
# hat the minimum depth would be found. Therefore, this results in a \mathcal{O}(N)O(N) complexity.
# One way to optimize the complexity is to use the BFS strategy. We iterate the tree level by level,
# and the first leaf we reach corresponds to the minimum depth. As a result, we do not need to iterate all nodes
from collections import deque


class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            node_deque = deque([(1, root), ])

        while node_deque:
            depth, root = node_deque.popleft()
            children = [root.left, root.right]
            if not any(children):
                return depth
            for c in children:
                if c:
                    node_deque.append((depth + 1, c))