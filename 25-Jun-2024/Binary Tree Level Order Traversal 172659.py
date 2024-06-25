# Problem: Binary Tree Level Order Traversal - https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root :
             return []
        res = []
        queue = deque([(root, 0)])


        while queue:
            node , lev = queue.popleft()
            if len(res) <= lev:
                res.append([])
            res[lev].append(node.val)

            if node.left:
                queue.append((node.left ,lev + 1))
            if node.right:
                queue.append((node.right , lev + 1))

        return res
            





         
            

        
