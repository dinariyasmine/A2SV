# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = len(nums) - 1
        target = last
        while last >= 0:
            if nums[last] >= target - last:
                target = last
            last -= 1
        return target == 0
        