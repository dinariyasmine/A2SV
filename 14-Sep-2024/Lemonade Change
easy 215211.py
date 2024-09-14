# Problem: Lemonade Change
easy - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dic = {5: 0, 10: 0, 20: 0}

        for bill in bills:
            if bill == 5:
                dic[5] += 1
            elif bill == 10:
                if dic[5] > 0:
                    dic[5] -= 1
                else:
                    return False
                dic[10] += 1

            elif bill == 20:
                dic[20] += 1
                if dic[10] > 0 and dic[5] > 0:
                    dic[10] -= 1
                    dic[5] -= 1

                elif dic[5] > 2:
                    dic[5] -= 3
                else: 
                    return False
                
        return True
                    


        
        return True
        