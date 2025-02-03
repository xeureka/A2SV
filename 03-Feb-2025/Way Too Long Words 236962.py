# Problem: Way Too Long Words - https://codeforces.com/problemset/problem/71/A

for i in range(int(input())):
    word = input()

    if len(word) <= 10:
        print(word)
    
    else:
        n = len(word) - 2

        print(f'{word[0]}{n}{word[len(word) - 1]}')