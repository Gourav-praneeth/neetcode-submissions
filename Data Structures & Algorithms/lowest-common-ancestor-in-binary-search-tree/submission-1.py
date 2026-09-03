# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
        given: a tree and two nodes p, q 
        return: lowest common ancestor
        1. A node can be decendent of itself.

        if p, q is < curr node go left
        if p,q is > cuur node go left
        if p < curr < q we found our LCA
        if p == curr and q == curr return p since it can be a decendent 
        '''
        

        while root:
            
            if p.val < root.val and q.val < root.val:
                root = root.left
              

            elif p.val > root.val and q.val > root.val:
                root = root.right
                
            else:
                return root


        