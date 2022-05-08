from collections import deque
import itertools

priorities = list(itertools.permutations(["-", "*", "+"], 3))

def calculate(x, y, op):
    if op == '*':
        return x * y
    if op == '-':
        return x - y
    if op == '+':
        return x + y


def solution(expression):
    answer = 0

    tmp_store = []
    numbers = []
    operators = []

    for i, c in enumerate(expression):
        if '0' <= c <= '9':
            tmp_store.append(c)
        else:
            operators.append(c)
            numbers.append(int(''.join(tmp_store)))
            tmp_store = []
    numbers.append(int(''.join(tmp_store)))

    for priority in priorities:
        next_numbers = numbers
        next_operators = operators
        for op in priority:
            tmp_numbers = [next_numbers[0]]
            tmp_operators = []
            for i, c in enumerate(next_operators):
                if c == op:
                    tmp_numbers.append(calculate(tmp_numbers.pop(), next_numbers[i+1], op))
                else:
                    tmp_numbers.append(next_numbers[i+1])
                    tmp_operators.append(c)
            next_numbers = tmp_numbers
            next_operators = tmp_operators
        answer = max(answer, abs(next_numbers[0]))

    return answer


expressions = ["100-200*300-500+20", "50*3-6*2", "1+2+3+4", "100*10-100", "200-300-500-600*40+500+500", "10-1000*100"]
# 60420
# 300

for expression in expressions:
    print(solution(expression))
