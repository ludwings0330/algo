def solution(citations):
    answer = 0

    citations.sort(reverse=True)
    n = len(citations)

    for i in range(n, -1, -1): # n편 ~ 1편
        answer = i
        flag = True
        for j in range(0, i):
            if citations[j] < i:
                flag = False # 더 찾아봐야한다는뜻.
                break
        if flag:
            break

    return answer

if __name__ =="__main__":
    # citations = [3, 0, 6, 1, 5]
    citations = [2, 2, 3, 5, 4, 5, 5, 5, 2]

    print("h-index = {}".format(solution(citations)))

