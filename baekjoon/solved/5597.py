students = set(i for i in range(1, 31))
for i in range(28):
    students.remove(int(input()))
a = students.pop()
b = students.pop()
if a > b:
    a, b = b, a
print(a, b, sep='\n')