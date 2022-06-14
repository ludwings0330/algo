import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
while t:
    t -= 1
    # number of candies
    n = int(input())
    candies = list(map(int, input().split()))

    moves = 1
    alice_idx = 1
    alice_previous = candies[0]
    alice_eat = candies[0]
    bob_idx = n -1
    bob_previous = 0
    bob_eat = 0

    #
    ALICE = 0
    BOB = 1

    turn = BOB

    while alice_idx <= bob_idx:
        if turn == ALICE:
            tmp_eat = 0
            while alice_idx <= bob_idx and tmp_eat <= bob_previous:
                tmp_eat += candies[alice_idx]
                alice_idx += 1
            alice_eat += tmp_eat
            alice_previous = tmp_eat
            moves += 1
            turn = BOB

        elif turn == BOB:
            tmp_eat = 0
            while alice_idx <= bob_idx and tmp_eat <= alice_previous:
                tmp_eat += candies[bob_idx]
                bob_idx -= 1
            bob_eat += tmp_eat
            bob_previous = tmp_eat
            moves += 1
            turn = ALICE

    print(moves, alice_eat, bob_eat)
