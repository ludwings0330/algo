def game(stone, round):
    if stone == 0:
        if round%2 == 1:
            print('CY')
        else:
            print('SK')
        return


    if stone%3 == 0 and stone - 3 >= 0:
        game(stone-3, round + 1)
    else:
        game(stone-1, round + 1)

# 이기려고 최선을 다할때
# 이긴 사람을 출력하시오
# 마지막 돌을 가져간 사람이 지게 된다
N = int(input())
cache = [-1] *(N+1)
(game(N, 0))
