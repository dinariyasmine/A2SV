# Problem: Vertical Order Traversal of a Binary Tree - https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            
            return []

        
        col_rank = defaultdict(list)

        
        def dfs(node,col,row):
            if not node:
                return

            col_rank[col].append((row,node.val))
            dfs(node.left,col -1,row +1)
            dfs(node.right,col +1,row +1)

        
        dfs(root,0,0)

        
        srtd = sorted(col_rank.items())
        answer =[]
        for col,nodes in srtd:
            
            nodes.sort(key=lambda x:(x[0],x[1]))
            curr =[]
            for row, val in nodes:
                curr.append(val)
            answer.append(curr)

        return answer