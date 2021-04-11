if __name__=="__main__":
    A, P = list(map(int, input().split()))

    tmp = A
    n = 0

    while tmp > 0:
        tmp = tmp//10
        n += 1

    stack = []
    answer = []
    visited = set()
    stack.append(A)
    visited.add(A) # 방문 표시

    while stack:
        node = stack.pop()
        answer.append(node)
        tmp = node
        nextnode = 0
        while tmp > 0:
            nextnode += (tmp%10)**P
            tmp = tmp//10

        if nextnode in visited: # 확인부터하고 넣어줘야지.
            # 만약에 이미 방문했어.
            # 그러면 이제 돌아가야지.
            while answer.pop() != nextnode:
                pass
            break
        stack.append(nextnode)
        visited.add(nextnode)
    print(len(answer))
    pass