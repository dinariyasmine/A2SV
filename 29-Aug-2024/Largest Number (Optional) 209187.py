# Problem: Largest Number (Optional) - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        str_num = [str(x) for x in nums]
        print(str_num)

        def compare(a, b):
            if a + b > b + a:
                return -1
            # b should come first then a
            elif a + b < b + a:
                return 1
            else:
                return 0
            
        str_num.sort(key=cmp_to_key(compare))

        if str_num[0] == '0':
            return '0'

        return ''.join(str_num)

        