import math
print(math.gcd(10, 20, 30))
print(math.lcm(10, 30, 70))


def gcd(A, B):
    if B == 0:
        return A
    return gcd(B, A%B)


print(gcd(6, 20))
x = 6
y = 20
print(x * y // gcd(x, y))
