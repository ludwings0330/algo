import sys

def input_data():
	readl = sys.stdin.readline
	N = int(readl())
	A = list(map(int, readl().split()))
	return N, A


sol = []

# 입력받는 부분
N, A = input_data()

# 0 1 2 3 4
# 1 3 5 7 9
# 1 3 9 7 5
# 여기서부터 작성
idx_list = [-1] * N
idx = 0
cnt = 0
i = 0
while cnt < N:
	if idx_list[idx] != -1: # 초기화 안되어있다면
		idx += 1
		idx %= N
		continue
	idx_list[i] = idx
	cnt += 1
	idx = (idx + A[idx]) % N
	i += 1

# 출력하는 부분
print(N)
print(*sol)