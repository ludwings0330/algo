def AA(s:str):
    print(s.upper(), end=' ')


def BB(k: int):
    print(k + 10)

a, b = input().split()
if a.isdigit():
    a, b = b, a

AA(a)
BB(int(b))
