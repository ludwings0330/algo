import sys
import heapq

if __name__ == "__main__":
    T = int(input())

    for i in range(T):
        k = int(sys.stdin.readline())
        data = []

        for j in range(k):
            command, num = sys.stdin.readline().split()
            num = int(num)
            if command == 'I':
                data.append(num)
            elif command == 'D':
                if len(data) == 0 :
                    pass
                elif num == 1: # 최대값 삭제.
                    data.remove(max(data))
                else: # command[1] == '-1' 최소값 삭제.
                    data.remove(min(data))

        if len(data) == 0:
            print('EMPTY')
        else:
            print(max(data), min(data))
