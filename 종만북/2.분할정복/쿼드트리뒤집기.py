C = int(input())

def rePack():
    global idx
    idx += 1
    if userInput[idx] !='x':
        return userInput[idx]

    topLeft = rePack()
    topRight = rePack()
    bottomLeft = rePack()
    bottomRight = rePack()

    return 'x' + bottomLeft + bottomRight + topLeft + topRight

for testCase in range(1, C+1):
    userInput = input()
    idx = -1

    print(rePack())

# xxwwwbxwxwbbbwwxxxwwbbbwwwwbb