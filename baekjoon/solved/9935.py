import sys
from collections import deque

iStr = input()
bStr = input()

ansStack = []
tmpStack = []
indexStack = []
for c in iStr:
    if not tmpStack: # 비어 있으면
        if c != bStr[0]:
            ansStack.append(c)
        else:
            if len(bStr) != 1:
                tmpStack.append(c) # 첫번째 글자가 같다는 뜻
                indexStack.append([1])
    else: # tmpStack 비어있지않으면
        t, index = tmpStack[-1], indexStack[-1]
        tmp = [1] if bStr[0]==c else []
        isbomb = False

        for i in index:
            if bStr[i] == c:
                tmp.append(i+1)
                if i+1 == len(bStr):
                    isbomb = True

        if not tmp: #tmp가 비어있으면
            tmpStack.append(c)
            ansStack += tmpStack
            tmpStack = []
            indexStack = []
        else: # tmp 안비어 있으면
            tmpStack.append(c)
            indexStack.append(tmp)
        if isbomb:
            for _ in range(len(bStr)):
                tmpStack.pop()
                indexStack.pop()
ansStack += tmpStack
if ansStack:
    print(''.join(ansStack))
else:
    print('FRULA')
