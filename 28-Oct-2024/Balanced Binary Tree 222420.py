# Problem: Balanced Binary Tree - https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def balanced(node):
            if not node:
                return 0
            left_h = balanced(node.left)
            right_h = balanced(node.right)
            if left_h == -1 or right_h == -1 or abs(left_h - right_h) > 1:
                return -1
            return max(left_h, right_h) + 1


        return balanced(root) != -1
        

