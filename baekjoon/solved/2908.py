a, b = list(input().split())
a = reversed(a)
b = reversed(b)
a=int(''.join(a))
b=int(''.join(b))
if a>b:
    print(a)
else:
    print(b)