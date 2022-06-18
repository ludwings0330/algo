import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
while t:
    t -= 1
    time, interval = input().split()
    interval = int(interval)
    h, m = map(int, time.split(':'))

    times = set()
    while (h, m) not in times:
        times.add((h, m))
        m += interval
        h += m // 60
        h %= 24
        m %= 60

    count = 0
    for hh, mm in times:
        hh = str(hh)
        if len(hh) < 2:
            hh = '0' + hh

        mm = str(mm)
        if len(mm) < 2:
            mm = '0' + mm
        mm = mm[::-1]
        if mm == hh:
            count += 1
    print(count)