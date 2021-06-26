H, Y = map(int, input().split())
rateList = [1.05, 1.2, 1.35]
years = [1, 3, 5]
def recursiveSolve(money, y):
    if y > Y:
        return 0
    elif y == Y:
        return money
    else:
        ret = money
        for i in range(3):
            ret = max(ret, recursiveSolve(int(money*rateList[i]), y+years[i]))

        return ret

print(recursiveSolve(H, 0))