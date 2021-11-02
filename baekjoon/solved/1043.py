import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# N : number of people
# M : number of party

truth = list(map(int, input().split()))

if truth[0] == 0:
    print(M)
else:
    truth = set(truth[1:]) #진실을 아는 사람을 담아둔다.

    parties = []

    # 같은 회의에 들어갔던 사람들 끼리 묶는다.??
    for _ in range(M):
        party = set(list(map(int, input().split()))[1:])
        if truth & party:
            # 파티에 진실을 아는 사람이 한명이라두 있으면 그 파티에 있는 사람들은 모두 진실을 안다.
            # 모두 진실에 추가해줘야함.
            truth.add(party)
            # 진실을 아는 사람에 변동이 생겻으므로
            # 진실을 아는 사람이 없는 파티에서 확인해봄

            for p in parties:
                # 진실을 아는 사람이 없는 모든 파티에서 반복
                # 진실을 아는 사람이 있는지 확인
                if truth & p: # 진실을 아는 사람이 있다면
                    truth.add(p) # 모두 추가해줌.
                    # 또 새로운 사람이 생겼으니까 또 확인해보고 추가해야한다?


        else:
            parties.append(party) # 진실을 아는 사람이 한명도 없으면 우선 parties 에 넣어둔다.
