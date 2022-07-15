k = int(input())
c = 0
for i in range(k):
    s = input()
    if "MINCO" in s:
        for j in range(len(s)):
            if j+5 <= len(s):
                if s[j:j+5] == "MINCO":
                    c += 1

print(c)