K = int(input())

# A -> B [1, 0] -> [0, 1]
# A*n -> B*n [n, 0] -> [0, n]
# B -> BA [0, 1] -> [1, 1]
# B*n -> BA*n [0, n] -> [n, n]

answer = [1, 0] # 최초 상태 'A'

while K:
    K -= 1
    answer = [answer[1], answer[0] + answer[1]]

print(" ".join(str(e) for e in answer))