from collections import defaultdict

def solution(steps_one, names_one, steps_two, names_two, steps_three, names_three):
    answer = []
    steps = [zip(steps_one, names_one), zip(steps_two, names_two), zip(steps_three, names_three)]

    total_score = defaultdict(int)

    for steps_day in steps:
        day_score = defaultdict(int)

        for step, name in steps_day:
            day_score[name] = max(day_score[name], step)
        for name, score in day_score.items():
            total_score[name] += score

    answer = sorted(total_score.items(), key=lambda x:(-x[1], x[0]))
    return [l[0] for l in answer]