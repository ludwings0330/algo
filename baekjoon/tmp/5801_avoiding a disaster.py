t = int(input())
while t:
    t -= 1

    clocks = input().split()
    clocks_minutes = [0] * 3
    cycle = 60 * 12
    for i, clock in enumerate(clocks):
        h, m = map(int, clock.split(":"))
        clocks_minutes[i] = (h * 60 + m)

    clocks_minutes.sort()
    gap = [0] * 3
    gap[0] = clocks_minutes[1] - clocks_minutes[0]
    gap[1] = clocks_minutes[2] - clocks_minutes[1]
    gap[2] = clocks_minutes[0] - clocks_minutes[2] + cycle

    if gap[0] == gap[1] == gap[2]:
        print("Look at the sun")
    elif gap[0] == gap[1] and gap[0] != gap[2]:
        print(f"The correct time is %d:%02d" %(clocks_minutes[1]//60, clocks_minutes[1] % 60))
    elif gap[1] == gap[2] and gap[1] != gap[0]:
        print(f"The correct time is %d:%02d" %(clocks_minutes[2]//60,clocks_minutes[2]%60))
    elif gap[2] == gap[0] and gap[2] != gap[1]:
        print(f"The correct time is %d:%02d" %(clocks_minutes[0]//60,clocks_minutes[0]%60))
    else:
        print("Look at the sun")