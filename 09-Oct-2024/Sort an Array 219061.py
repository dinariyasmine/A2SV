# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        mini = min(nums)
        maxi = max(nums)
        cpt = maxi - mini + 1
        buckets = [[] for _ in range(cpt)]
        ans = []
        for num in nums:
            idx = num - mini
            buckets[idx].append(num)
        #insertion sort
        for bucket in buckets:
            for j in range(1, len(bucket)):  
                k1 = bucket[j]
                k = j - 1
                while k >= 0 and bucket[k] > k1:
                    bucket[k + 1] = bucket[k]
                    k -= 1
                bucket[k + 1] = k1
            ans.extend(bucket)
        return ans
