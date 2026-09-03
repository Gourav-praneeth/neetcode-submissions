# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        queue = deque([(root, root.val)])

        while queue:
            
            node, pathSum = queue.popleft()

            if not node.left and not node.right:
                if pathSum == targetSum:
                    return True

            if node.left:
                queue.append((node.left, node.left.val + pathSum))

            if node.right:
                queue.append((node.right, node.right.val + pathSum))     

        return False
