def solution(price, money, count):
    return max(0, count*(2*price + (count-1)*price)//2 - money)

print(solution(3,20,4))