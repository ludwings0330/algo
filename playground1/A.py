import sys
input = sys.stdin.readline

T = int(input())

words = [[0] * 13 for _ in range(3)]
key = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
for i in range(3):
    for j in range(i+1, len(key[i])+i+1):
        words[i][j] = key[i][j-(i+1)]

def move():
    pass

while T:
    T -= 1
    strInput = input().rstrip()
    ret = 1

    for i in range(1, len(strInput)):
        ret += move(strInput(i))
        ret += 1

    print(ret)

