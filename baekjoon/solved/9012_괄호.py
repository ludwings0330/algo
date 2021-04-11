import sys
if __name__ == "__main__":
    N = int(input())
    for i in range(N):
        inputStr = sys.stdin.readline().rstrip()
        count = 0
        for j in list(inputStr):
            if j == '(':
                count += 1
            elif j == ')':
                count -= 1
            if count < 0:
                break
        if count == 0:
            print('YES')
        else:
            print('NO')