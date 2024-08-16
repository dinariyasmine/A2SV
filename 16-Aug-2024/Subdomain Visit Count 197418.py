# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count/description/

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_cpt = defaultdict(int)
        
        for cpdomain in cpdomains:
            cpt, domain = cpdomain.split(" ")
            cpt = int(cpt)
            
            subdomains = domain.split(".")          
            for i in range(len(subdomains)):
                subdomain = ".".join(subdomains[i:])
                domain_cpt[subdomain] += cpt

        res = [str(cpt) + " " + subdomain for subdomain, cpt in domain_cpt.items()]
        
        return res