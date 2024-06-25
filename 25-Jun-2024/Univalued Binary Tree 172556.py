# Problem: Univalued Binary Tree - https://leetcode.com/problems/univalued-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        val = root.val
        queue = deque([root])
        while queue:
            inter = queue.popleft()
            if inter.val != val:
                return False
            else:
                if inter.right:
                    queue.append(inter.right)
                if inter.left:
                    queue.append(inter.left)
        return True
            
        