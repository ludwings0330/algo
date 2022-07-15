a, b, c = map(int, input().split())
print('inssa' if (a < b and b < c) or (c < b and b < a) else 'assa sin nanda')
