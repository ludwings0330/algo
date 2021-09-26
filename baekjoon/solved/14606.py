def pizza(height):
    if height == 1:
        return 0

    a = height//2
    b = a

    if height%2 == 1:
        b += 1

    ret = a*b
    ret += pizza(a)
    ret += pizza(b)

    return ret

n = int(input())
print(pizza(n))