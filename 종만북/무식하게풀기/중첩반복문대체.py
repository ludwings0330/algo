def pick(n: int, picked: list, to_pick: int) -> None:
    if to_pick == 0:
        print(*picked)
        return

    smallest = picked[-1] if picked else -1

    for next in range(smallest+1, n):
        pick(n, picked + [next], to_pick-1)


pick(7, [], 4)
