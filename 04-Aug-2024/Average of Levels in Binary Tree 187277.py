# Problem: Average of Levels in Binary Tree - https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        res = []
        visited =  defaultdict(list)

        dq = deque([(root,0)])
        visited[0].append(root.val)

        


        while dq:
            
            (curr, level) = dq.popleft()
            visited[level].append(curr.val)

            if curr.left != None:
                dq.append((curr.left, level + 1))
            if curr.right != None:
                dq.append((curr.right, level + 1))

            
        for level in visited:
            res.append(sum(visited[level])/len(visited[level]))

        return res

            

