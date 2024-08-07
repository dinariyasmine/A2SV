# Problem: Find Three Consecutive Integers That Sum to a Given Number - https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        start = (num - 3) // 3
        
        if start * 3 + 3 == num:
            return [start, start + 1, start + 2]
        else:
            return []