# Problem: Convert Sorted Array to Binary Search Tree  - https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def inter(left,right):
            if left > right:
                return None

            mil = (left+right)//2
            node = TreeNode(nums[mil])
            node.left = inter(left, mil-1)
            node.right = inter(mil+ 1, right)

            return node


        return inter(0, len(nums) - 1)
