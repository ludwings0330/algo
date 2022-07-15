input_list = list(map(int, input().split()))

flag = False
total = 0
for num in input_list:
    if num == 7:
        flag = True
    else:
        total += num
print('lucky' if flag else '')
print(total)