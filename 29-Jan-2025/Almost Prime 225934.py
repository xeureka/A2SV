# Problem: Almost Prime - https://codeforces.com/problemset/problem/26/A



n = int(input())

def prime(num:int):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True


count = 0


for item in range(2,n+1):
    temp = [i for i in range(2,item) if item % i == 0 and prime(i)]

    if len(temp) == 2:
        count += 1

print(count)