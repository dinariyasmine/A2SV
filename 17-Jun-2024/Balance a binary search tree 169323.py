# Problem: Balance a binary search tree - https://leetcode.com/problems/balance-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, node, res):
        if not node :
            return
        self.inorder(node.left,res)
        res.append(node.val)
        self.inorder(node.right,res)
        
    def balanceBST(self, root: TreeNode ) -> TreeNode:
        def bbst(srt):
            if not srt:
                return None
            mid=len(srt)// 2
            root=TreeNode(srt[mid])
            root.left=bbst(srt[:mid])
            root.right=bbst(srt[mid+1:])
            return root

        srt=[]
        self.inorder(root,srt)
        print(srt)
        return bbst(srt)


