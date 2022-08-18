a, b = map(int, input().split())
print(0 if a * (1-b/100) >= 100 else 1)