# Problem: Replace Elements with Greatest Element on Right Side - https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n= len(arr)

        if n== 0:
            return arr
        
        g= -1
        for i in range(n-1,-1,-1):
            
            curr=arr[i]
            arr[i]=g
            if curr > g:
                g=curr
        
        return arr
