# Problem: Thearte Square - https://codeforces.com/problemset/problem/1/A

from math import ceil

n,m,a = map(int,input().split())

right = ceil(n/a)
left = ceil(m/a)

print(int(right*left))