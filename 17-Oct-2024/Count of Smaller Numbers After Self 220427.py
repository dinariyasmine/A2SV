# Problem: Count of Smaller Numbers After Self - https://leetcode.com/problems/count-of-smaller-numbers-after-self/

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        cpt = [0] * len(nums)
        idx = [(nums[k_idx], k_idx) for k_idx in range(len(nums))]
        desc_nums, cpt = self.mergeWcpt(idx, cpt)
        return cpt
	
	
    def mergeWcpt(self, nums, cpt):
        if len(nums) == 1:
            return nums, cpt

        curr = []
        left, cpt = self.mergeWcpt(nums[: len(nums) // 2], cpt)
        right, cpt = self.mergeWcpt(nums[len(nums) // 2 :], cpt)
        
        
        while left and right:
            
            if left[0] > right[0]:
                cpt[left[0][1]] += len(right)
                curr.append(left.pop(0))
            else:
                curr.append(right.pop(0))
                
        if left:
            curr.extend(left)
        else:
            curr.extend(right)
			
        return curr, cpt