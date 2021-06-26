import sys
input = sys.stdin.readline

N = int(input())
arr = {}

for i in range(N):
    index = int(input())
    if index in arr:
        arr[index] += 1
        continue
    arr[index] = 1
sortedKeys = sorted(arr.keys())

for i in sortedKeys:
    print((str(i)+'\n')*arr[i], end='')