# MIN heap
import sys

if __name__ == "__main__":
    N = int(input())
    heap = [0]
    cnt = 0
    for i in range(N):
        command = int(sys.stdin.readline().rstrip())
        if command == 0:
            if cnt > 0: # 데이터가 존재한다면
                heap[1], heap[-1] = heap[-1], heap[1] # 맨마지막놈하고 교환
                print(heap.pop())
                cnt -= 1
                # 출력했으니 다시 힙을 정렬해 줘야지.
                # 왼쪽자식 index*2 , 오른쪽자식 index*2 + 1
                index = 1
                while True:
                    left = index*2
                    right = index*2 + 1
                    MIN = left
                    if left > cnt: # 왼쪽자식없으면 break 지.
                        break
                    elif right <= cnt: # 오른쪽 자식이 존재하면
                        if heap[MIN] > heap[right]:
                            MIN = right
                    if heap[MIN] < heap[index]:
                        heap[MIN], heap[index] = heap[index], heap[MIN]

                    index = MIN
            else: # 데이터가 없으면
                print(0)


            pass
        else:
            heap.append(command)
            cnt += 1
            index = cnt
            while index > 1:
                if heap[index] < heap[index//2]:  # 자식이 부모보다 작으면 교환
                    heap[index], heap[index//2] = heap[index//2], heap[index]
                    index //= 2
                else:
                    break
