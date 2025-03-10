# Problem: Less or Equal - https://codeforces.com/problemset/problem/977/C


n,k = map(int,input().split())

lst = list(map(int,input().split()))

lst.sort()

if k == 0:
    if lst[0] > 1:
        print(lst[0]-1)
    
    else:
        print(-1)

else:
    num = lst[k-1]
    cnt = 0

    for i in lst:
        if i <= num:
            cnt += 1
    
    if cnt == k:
        print(num)
    else:
        print(-1)







