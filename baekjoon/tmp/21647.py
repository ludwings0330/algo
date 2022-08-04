w, b = map(int, input().split())
ans = ['    ']
idx = 4

while True:
    try:
        tmp = input().split()
        if not tmp:
            ans.append('\n' + ' ' * b)
            idx = b
            continue

        for i in range(len(tmp)):
            if idx +1 +  len(tmp[i]) > w:
                ans.append('\n' + tmp[i])
                idx = len(tmp[i])
            else:
                ans.append(' ' + tmp[i])
                idx += len(tmp[i]) + 1
    except EOFError:
        print(''.join(ans))
        break