n = 6
result = 0
for i in range(1, n+1):
    result += i
print(result)


def recursive_sum(i):
    if i == 1:
        return 1

    return i + recursive_sum(i-1)


print(recursive_sum(n))