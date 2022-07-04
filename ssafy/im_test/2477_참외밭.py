melon = int(input())
answer = 0

sub_area = 1
max_w = 0
max_w_idx = -1
max_h = 0
max_h_idx = -1
store = []
for i in range(6):
    d, l = map(int, input().split())
    store.append(l)

    if d == 3 or d == 4:
        if max_h < l:
            max_h = l
            max_h_idx = i
    elif d == 1 or d == 2:
        if max_w < l:
            max_w = l
            max_w_idx = i

sub_w = abs(store[max_w_idx-1] - store[(max_w_idx + 1) % len(store)])
sub_h = abs(store[max_h_idx-1] - store[(max_h_idx + 1) % len(store)])
total_area = max_w * max_h
sub_area = sub_w * sub_h

answer = total_area - sub_area
answer *= melon

print(answer)
