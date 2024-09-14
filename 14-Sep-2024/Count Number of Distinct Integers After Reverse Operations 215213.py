# Problem: Count Number of Distinct Integers After Reverse Operations - https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/

class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        distinct = set()

        for num in nums:
            ans = int(str(num)[::-1])
            distinct.add(num)
            distinct.add(ans)

        return len(distinct)
