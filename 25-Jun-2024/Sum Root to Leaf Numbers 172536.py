# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def concatene(nbrs):
            return int(''.join(str(nbr) for nbr in nbrs))

        def dfs(root,path,summ):
            if root is None:
                return 0

            path.append(root.val)

            if not root.right and not root.left :
                return concatene(path)
                
            summ = 0
            
            if root.right:
                summ += dfs(root.right,path[:],summ)
            if root.left:
                summ += dfs(root.left,path[:],summ)
                
            return summ

            

        return dfs(root,[],0)
        



            



        