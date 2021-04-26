
import sys, heapq
ipt = sys.stdin.readline
opt = sys.stdout.write
t = int(ipt())

for _ in range(t):
    k = int(ipt())
    max_h, min_h = [], []
    count_dict = dict()
    for _ in range(k):
        op, n = ipt().split()
        n = int(n)
        if op == 'I':
            if n in count_dict:
                count_dict[n] += 1
            else:
                count_dict[n] = 1
            heapq.heappush(min_h, n)
            heapq.heappush(max_h, -n)
        elif op == 'D':
            if n == 1:
                while max_h:
                    c = -heapq.heappop(max_h)
                    if c in count_dict and count_dict[c] > 0:
                        count_dict[c] -= 1
                        if not count_dict[c]:
                            del count_dict[c]
                        break
            else:
                while min_h:
                    c = heapq.heappop(min_h)
                    if c in count_dict and count_dict[c] > 0:
                        count_dict[c] -= 1
                        if not count_dict[c]:
                            del count_dict[c]
                        break
    if count_dict:
        sorted_items = sorted(count_dict.items())
        opt(f'{sorted_items[-1][0]} {sorted_items[0][0]}\n')
    else:
        opt('EMPTY\n')