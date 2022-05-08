# 미세먼지 농도가 어느 하나라도 나쁨이면 마스크 착용
# 새마스크는 이틀 후 까지만 재사용 (3일 사용, 3일째에 폐기)
# 미ㄴ미세먼지, 초미세먼지 농도가 둘 다 매우나쁨이면 마스크를 그날 까지만 쓰고 재사용 X

# 1 : bad
# 2 : very bad

def judge_airquality(state):
    dust = 0
    find_dust = 0
    if state[0] >= 151:
        dust = 2
    elif state[0] >= 81:
        dust = 1

    if state[1] >= 76:
        find_dust = 2
    elif state[1] >= 36:
        find_dust = 1

    return [dust, find_dust]


def solution(atmos):
    answer = 0
    remain = 0
    for day, state in enumerate(atmos):
        air_quality = judge_airquality(state)

        # 둘중에 하나라도 나쁨이면
        if air_quality[0] > 0 or air_quality[1] > 0:

            # 둘다 매우 나쁨이면
            if air_quality[0] > 1 and air_quality[1] > 1:
                if remain <= 0:
                    # 사용하고 즉시 폐기
                    answer += 1
                else:
                    # 그날 바로 폐기
                    remain = 0
            # 하나만 나쁨이면
            else:
                if remain > 0:
                    # 사용중인 마스크가 있다면 remain 을 하나 줄인다
                    remain -= 1
                else:
                    # 사용중인 마스크가 없다면 새로 할당
                    answer += 1
                    remain = 2
        else:
            remain -= 1
    return answer


# [ 미세먼지, 초미세 먼지 ]
atmos = [[[80, 35], [70, 38], [100, 41], [75,30], [160,80], [77, 29], [181, 68], [151, 76]],
          [[140, 90], [177, 75], [95, 45], [71, 31], [150, 30], [80, 35], [72, 33], [166, 81], [151, 75]],
          [[30, 15], [80, 35]]]

for atmo in atmos:
    print(solution(atmo))
