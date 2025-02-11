# Problem: Same Differences - https://codeforces.com/problemset/problem/1520/D

from collections import defaultdict




for i in range(int(input())):

    n = int(input())

    lst = list(map(int, input().split()))

    ans = 0

    dd = defaultdict(int)



    for i, v in enumerate(lst):

        dd[v-i] += 1

        



    for v in dd.values():

        if v > 1:

            ans += v*(v-1)//2



    print(ans)
