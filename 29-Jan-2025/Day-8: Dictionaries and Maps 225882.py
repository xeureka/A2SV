# Problem: Day-8: Dictionaries and Maps - https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem

# dictionary and map


# name = phoneNumber
# name aint exit Not Found

# phone book should be hasmap(dictionary)


hasmap = {}

n = int(input())

for i in range(n):
    name,phone = map(str,input().split())
    hasmap[name] = phone


while True:
    try:
        name = input()
        if name in hasmap:
            print(f'{name}={hasmap[name]}')
        else:
            print('Not found')
    except EOFError:
        break