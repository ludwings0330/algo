TC = int(input())

while TC:
    TC -= 1
    note_a, note_b = input().rstrip().split()
    note_b = int(note_b)

    color_a = 'B' if ((ord(note_a[0]) - 65)%2 + int(note_a[1]) % 2) == 1 else 'W'
    color_b = 'B' if ((note_b-1)//8 + note_b%2) % 2 == 1 else 'W'

    if color_a == color_b:
        print('YES')
    else:
        print('NO')

