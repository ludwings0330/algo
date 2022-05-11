from collections import defaultdict
def solution(fees, records):
    base_time, base_fee, interval_time, interval_fee = fees

    store = {}
    parking_time_dict = defaultdict(int)
    answer = []
    for record in records:
        in_time, number, option = record.split()
        in_time = int(in_time.split(":")[0]) * 60 + int(in_time.split(":")[1])

        if option == "IN":
            store[number] = in_time

        elif option == "OUT":
            out_time = store[number]
            parking_time_dict[number] += in_time - out_time
            del(store[number])

    if store:
        for number, time in store.items():
            in_time = "23:59"
            in_time = int(in_time.split(":")[0]) * 60 + int(in_time.split(":")[1])
            out_time = store[number]
            parking_time_dict[number] += in_time - out_time

    import math
    for number in sorted(parking_time_dict.keys()):

        answer.append(base_fee + max(0, math.ceil((parking_time_dict[number]-base_time)/interval_time)) * interval_fee)
    return answer

# 요금표, 입차, 출차 시간이 있을때 차량별로 주차 요금 계산

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))