# Problem: Fair Distribution of Cookies - https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        def btrac(idx, grps):
            if idx == len(cookies):
                return max(grps)

            mini=float('inf')
            for i in range(k):
                grps[i]+=cookies[idx]
                mini=min(mini,btrac(idx+1,grps))

                grps[i] -=cookies[idx]
                if grps[i]== 0:
                    break
            
            return  mini
        
        return btrac(0,[0]*k)

