# Problem: Team - https://codeforces.com/contest/231/problem/A

answer = 0
 
 
for i in range(int(input())):
    
    lst = list(map(int,input().split()))
    
    if lst.count(1) >= 2:
        answer += 1
 
    
print(answer)