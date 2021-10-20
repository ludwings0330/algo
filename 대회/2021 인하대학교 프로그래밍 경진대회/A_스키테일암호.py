K = int(input())
code = input()
ans = ""
for i in range(0, len(code), K):
    ans += code[i]
print(ans)
