input()
A = input()
B = input()

if len(A) < len(B):
    A, B = B, A

found = False
for i in range(len(B), -1, -1):
    for start in range(0, len(B) - i):
        if B[start:start+i] in A:
            print(B[start:start+i])
            found = True
            break
    if found:
        break