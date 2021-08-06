from  collections import deque

def solution(arr, k):
    answer = -1

    order = [i for i in range(1, len(arr)+1)]

    dq = deque()
    visit = set()
    dq.append([0, arr])
    visit.add(tuple(arr))

    while dq:
        node = dq.popleft()
        c = node[0]
        tarr= node[1]
        if tarr == order:
            answer = c
            break

        for i in range(len(arr)):
            for j in range(i+1, min(len(arr), i+k+1)):
                if tarr[i] > tarr[j]: # 앞에 있는게 더 크면 교환
                    tarr[j], tarr[i] = tarr[i], tarr[j]
                    if tuple(tarr) not in visit:
                        visit.add(tuple(tarr))
                        dq.append([c+1, tarr[:]])
                    tarr[j], tarr[i] = tarr[i], tarr[j] # 넣어주고 다시 교환


    return answer

arr= [[4,5,2,3,1], [5,4,3,2,1], [5,4,3,2,1], [7,6,5,4,3,2,1],
      [7,6,5,4,3,2,1],[7,6,5,4,3,2,1],[7,6,5,4,3,2,1], [1, 2, 3, 4, 5, 6, 7]]
k = [2, 4, 2, 1, 2, 3, 4, 5]

for i in range(len(arr)):
    print(solution(arr[i], k[i]))