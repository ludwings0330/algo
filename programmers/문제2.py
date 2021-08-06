def solution(words):
    answer = 0
    graph = {}

    for word in words:
        if word[0] not in graph:
            graph[word[0]] = [dict(), 1]
        else:
            graph[word[0]][1] += 1
        node = graph[word[0]]

        for i in range(1, len(word)):
            if word[i] not in node[0]:
                node[0][word[i]] = [dict(), 1]
            else:
                node[0][word[i]][1] += 1
            node = node[0][word[i]]

    for word in words:
        node = graph[word[0]]
        answer += 1
        if node[1] == 1:
            continue
        for i in range(1, len(word)):
            if node[0][word[i]][1] == 1:
                answer += 1
                break
            node = node[0][word[i]]
            answer += 1
    return answer


words = [["go","gone","guild"], ["abc","def","ghi","jklm"], ["word","war","warrior","world"]]

for w in words:
    print(solution(w))
