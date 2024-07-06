# Problem: Sum of Nodes with Even-Valued Grandparent - https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def dfs(node,p,gp):
            if not node:
                return 0
            
            res= 0

            if gp and gp.val % 2 ==0:

                res +=node.val
            
            res +=dfs(node.left, node, p)
            res +=dfs(node.right, node, p)
            

            return res
        

        return dfs(root,None,None)