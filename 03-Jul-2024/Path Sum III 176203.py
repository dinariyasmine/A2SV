# Problem: Path Sum III - https://leetcode.com/problems/path-sum-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, curr):

            if not node  :

                return 0
            
            curr+= node.val

            nbr_Path= pSum[curr-targetSum]
            pSum[curr] +=1

            nbr_Path+= dfs(node.left,curr)
            nbr_Path+= dfs(node.right,curr)

            pSum[curr]-=1
            
            return nbr_Path


        
        pSum=defaultdict(int)
        pSum[0]=1
        
        return dfs(root,0)