arr = set(list(map(int, input().split())))
l = len(arr)
if l == 3:
    print('모두 다르다')
elif l == 2:
    print('일부 같다')
else:
    print('모두 같다')
