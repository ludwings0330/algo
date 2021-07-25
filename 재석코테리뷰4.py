for N in range(20):
    bornDragon = [0, 0, 1] # 오늘 태어난 드래곤
    eggs = [1, 0, 1] # 오늘 낳은 알
    nowDragon = 1
    totalDragon = 1
    for day in range(3, N+1):
        bornDragon.append(eggs[day-2]) # 알은 2일 후에 부화합니다.
        nowDragon += bornDragon[day]  # 현재드래곤 수는 부화한놈만큼 더한다
        totalDragon += bornDragon[day]
        eggs.append(nowDragon) # 모든 드래곤이 알을 낳는다.
        nowDragon -= bornDragon[day - 3] # 드래곤은 4번 알을 낳으면 죽는다
    if N == 0:
        pass
    elif N == 1:
        pass
    else:
        print("------------day", N, '--------------')
        print("answer :", totalDragon + eggs[-1] + eggs[-2], "dragon : ", totalDragon, "eggs : ", eggs[-1]+eggs[-2]) # 남은 알은 오늘 낳은 알 + 어제 낳은 알 , 드래곤의수는 지금 드래곤의 수
