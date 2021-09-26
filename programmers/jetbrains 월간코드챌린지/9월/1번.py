import sys
input = lambda: sys.stdin.readline().rstrip()

def solutions(numbers):
    answer = 0
    numbers = set(numbers)
    exNumbers = set([0,1,2,3,4,5,6,7,8,9])^numbers

    return sum(exNumbers)

print(solutions([1,2,3,4,6,7,8,0]))