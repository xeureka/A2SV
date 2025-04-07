# Problem: Sereja and Dima - https://codeforces.com/problemset/problem/381/A

def solve(lst:list):

    i,j = 0,len(lst)-1

    s,d = 0,0
    turn = True

    while i <= j:
        
        if lst[i] > lst[j]:
            val = lst[i]
            i += 1
        
        else:
            val = lst[j]
            j -= 1
        

        if turn:
            turn = False
            s += val
        
        else:
            turn = True
            d += val
    
    print(*[s,d])


    


n = int(input())
lst = list(map(int,input().split()))


solve(lst)