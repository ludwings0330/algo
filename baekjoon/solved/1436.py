N = int(input())

def check(s):
    for i in range(len(s)-2):
        if s[i:i+3] == '666':
            return True
    return False
count = 0
n = 0
while count < N:
    n += 1
    if check(str(n)):
        count += 1

print(n)