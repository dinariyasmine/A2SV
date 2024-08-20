# Problem: Range Sum of BST - https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def inorderSum(node):
            if not node:
                return 0
            
            leftSum = inorderSum(node.left)
            rightSum = inorderSum(node.right)

            currSum = node.val if low <= node.val <= high else 0

            return leftSum + currSum + rightSum
                 
        
        return inorderSum(root)