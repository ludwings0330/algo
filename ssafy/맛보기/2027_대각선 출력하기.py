for r in range(5):
    for c in range(5):
        if r == c:
            print('#', end='')
        else:
            print('+', end='')
    print()