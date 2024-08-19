# Problem: B - Make it Divisible by 25 - https://codeforces.com/gym/543262/problem/B

def div(idx, ending):
    if len(ending) == 2:
        if ending in ['00', '25', '50', '75']:
            return 0
        return float('inf')
    
    if idx < 0:
        return float('inf')
    
    if (idx, ending) in memo:
        return memo[(idx, ending)]
    
    exculde = float('inf')
    include = div(idx - 1, nbr[idx] + ending)
    
    if include > 0:
        exculde = 1 + div(idx - 1, ending)
    memo[(idx, ending)] = min(include, exculde)
    return memo[(idx, ending)]
    
    
    
t = int(input())
for _ in range(t):
    nbr = input()
    memo = {}
    res = div(len(nbr) - 1, "")
    print(res)