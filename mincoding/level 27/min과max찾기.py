arr = list(map(int, input().split()))
arr.sort()
query = list(input())
s = 0
e = len(arr)-1
for q in query:
    if q == 'm':
        print(arr[s], end='')
        s+=1
    else:
        print(arr[e], end='')
        e-=1