def SAMSUNG(alpha: str):
    return alpha.upper()


def MinCo(num:int):
    alpha = SAMSUNG(list("0ABCDEFGHIJKLNMOPQRSTUVWXYZ")[num])
    return chr(ord(alpha)+1)


def SSAFY(num:int):
    return MinCo(num)







n = int(input())
print(SSAFY(n))