M = int(input())
N = int(input())

min_num = float('inf')
total = 0
for num in range(M, N+1):
    if num**0.5 == int(num**0.5):
        total += num
        min_num = min(min_num, num)

print(f'{total}\n{min_num}' if min_num < float('inf') else f'-1')