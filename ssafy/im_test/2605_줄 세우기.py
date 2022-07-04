N = int(input())
answer = [1]
numbers = list(map(int, input().split()))

for i in range(1, N):
    number = numbers[i]
    answer = answer[:len(answer) - number] + [i+1] + answer[len(answer) - number:]

print(*answer)
