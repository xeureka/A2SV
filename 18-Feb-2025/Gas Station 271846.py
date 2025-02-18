# Problem: Gas Station - https://leetcode.com/problems/gas-station/

from collections import defaultdict



names = []

for i in range(int(input())):
    name = input()  
    names.append(name)


dd = defaultdict(int)

for i in range(len(names)-1,-1,-1):
    dd[names[i]] += 1



for key in dd.keys():
    print(key)




    