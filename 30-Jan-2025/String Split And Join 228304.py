# Problem: String Split And Join - https://www.hackerrank.com/challenges/python-string-split-and-join?isFullScreen=true

def split_and_join(line):
    # write your code here
    new_word = '-'.join(line.split())
    return new_word

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)