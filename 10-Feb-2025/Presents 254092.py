# Problem: Presents - https://codeforces.com/problemset/problem/136/A

n = int(input())

lst = list(map(int,input().split()))

hm = {}

for i,j in enumerate(lst):
    hm[j] = i + 1


for i in range(n):
    print(hm[i+1],end=' ')