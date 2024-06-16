# Problem: Valid Mountain Array - https://leetcode.com/problems/valid-mountain-array/description/

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n<3:
            return False
        p = 0
        while p+1<n and arr[p]<arr[p + 1]:
            p += 1
        if p ==0 or p ==n- 1:
            return False
        while p + 1 < n and arr[p] > arr[p + 1]:
            p+= 1
        
        return p==n-1