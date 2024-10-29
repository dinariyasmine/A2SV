# Problem: Binary Tree Right Side View - https://leetcode.com/problems/binary-tree-right-side-view/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        dq = deque([(root, 0)])
        res = []
        
        while dq:
            curr1, d1 = dq.popleft()
            if dq:
                curr2, d2 = dq[0]
                if d1 < d2:
                    res.append(curr1.val)
            else:
                res.append(curr1.val)
            if curr1 and curr1.left:
                dq.append((curr1.left, d1 + 1))
            if curr1 and curr1.right:
                dq.append((curr1.right, d1 + 1))
        return res

        