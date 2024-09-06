# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1

        email_to_id = {} 
        email_to_name = {}  
        n = 0  

        # give an id to each email ( as a  node)
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in email_to_id:
                    email_to_id[email] = n
                    n += 1
                email_to_name[email] = name

        parent = list(range(n))  
        rank = [0] * n  

        #connect same emails with same name 
        for account in accounts:
            first_email = account[1]

            for email in account[2:]:
                # we get the id of the email
                email_id = email_to_id[email]
                # and the representer of the group is the first email , we do union
                union(email_to_id[first_email], email_id)


        rep_to_emails = {}
        
        for email, idx in email_to_id.items():
            rep = find(idx)
            if rep not in rep_to_emails:
                rep_to_emails[rep] = []
            rep_to_emails[rep].append(email)

        res = []
        for rep, emails in rep_to_emails.items():
            name = email_to_name[emails[0]]
            res.append([name] + sorted(emails))

        return res
