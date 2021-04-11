import sys

if __name__ == "__main__":
    T = int(input())
    data = [1,2,3]

    def DFS(n):
        stack = []
        count = 0
        stack.append([1, 0])
        stack.append([2, 0])
        stack.append([3, 0])
        while stack:
            node = stack.pop()

            if node[0] + node[1] == n:
                count += 1

            for i in data:
                if node[0] + node[1] + i <= n:
                    stack.append([i, node[0]+node[1]])
        return count

    for i in range(T):
        N = int(sys.stdin.readline().rstrip())
        print(DFS(N))