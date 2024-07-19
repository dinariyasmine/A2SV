# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        if not root:
            return []
        
        dq = deque([root])
        res = []

        left_right = True
        
        while dq:
            depth = len(dq)
            level =[]
            
            for _ in range(depth):
                curr = dq.popleft()
                if curr:


                    level.append(curr.val)
                    dq.append(curr.left)
                    dq.append(curr.right)
            
            if level:

                if not left_right:
                    level.reverse()
                res.append(level)
            


            left_right = not left_right
        
        return res


