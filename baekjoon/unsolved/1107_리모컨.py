N = int(input())
M = int(input())
broken = list(map(int, input().split()))

# 현재 채널 100
MIN = N - 100

channelBig = N
countBig = 0

channelSmall = N
countSmall = 0

digit = 0
tmp = N
while tmp:
    tmp //= 10
    digit += 1

while channelBig < 1000001:
    channelBig += 1
    countBig += 1
    tmpChannel = channelBig
    while tmpChannel:
        i = tmpChannel%10
        if i in broken:
            break
        tmpChannel //= 10
    if tmpChannel == 0:
        # 모든 번호가 broken에 없다는 뜻.
        break


while channelSmall>0:
    channelSmall -= 1
    countSmall += 1
    tmpChannel = channelSmall
    while tmpChannel:
        i = tmpChannel%10
        if i in broken:
            break
        tmpChannel //= 10
    if tmpChannel == 0:
        # 모든 번호가 broken에 없다는 뜻.
        break
countBig += digit
countSmall += digit
MIN = min(MIN, countBig, countSmall)
print(MIN)