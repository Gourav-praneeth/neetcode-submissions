# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        level order + swapping
        '''
        res = []
        queue = deque([root])
        count = 0

        while queue:
            lev = []
            for _ in range(len(queue)):
                if not root:
                    return []
                node = queue.popleft()
                lev.append(node.val)

                # if count % 2 == 1:
                #     node.left, node.right = node.right, node.left

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            if count % 2 == 1:
                res.append(reversed(lev))
            else:
                res.append(lev)
            count += 1

        return res
                

