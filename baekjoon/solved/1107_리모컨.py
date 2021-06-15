import sys
input = sys.stdin.readline

N = input().rstrip()
M = int(input())
buttonsX = []
if M > 0:
    buttonsX = list(map(int, input().split()))
buttons = []
MIN = abs(int(N)-100) # + 혹은 - 버튼만 눌렀을때 가능한 횟수
if M == 10:
    print(MIN)

else:
    # 이제 가장 가까운 채널로 이동한 후에 +, - 버튼을 누르는 횟수
    for i in range(10):
        if i in buttonsX:
            continue
        buttons.append(i)

    for ch in range(100000):
        for i in range(len(str(ch))):
            if int(str(ch)[i]) not in buttons:
                break
            elif len(str(ch)) - 1 == i:
                MIN = min(MIN, abs(ch-N) + len(str(ch)))
    print(MIN)