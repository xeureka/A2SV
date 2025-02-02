# Problem: Sum - https://codeforces.com/contest/1742/problem/A

for i in range(int(input())):
    a,b,c = map(int,input().split())

    if a + b == c or b + c == a or a + c == b:
        print('YES')
    else:
        print('NO')