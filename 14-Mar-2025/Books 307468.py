# Problem: Books - https://codeforces.com/contest/279/problem/B



def solve(t,lst):

    i = 0
    j = 0
    ans = 0
    idx = 0

    while idx < len(lst):

        while i < len(lst) and j + lst[i] <= t:
            j += lst[i]
            i += 1
        
        ans = max(ans, i - idx)
        
        j -= lst[idx]
        idx += 1

    return ans

n,t = map(int,input().split())

lst = list(map(int,input().split()))


print(solve(t,lst))

                


