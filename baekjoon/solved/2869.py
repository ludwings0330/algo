import math
A, B, V = map(int, input().split())
k = (V-B) / (A-B)
k = math.ceil(k)
print(k)