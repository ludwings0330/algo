class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        # 1 <= logs.length <= 100
        # 3 <= logs[i].length <= 100
        digit_logs = []
        letter_logs = []

        for log in logs:
            identifier, content = log[:log.find(' ')], log[log.find(' ') + 1:]
            if content[0].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append([identifier, content])

        letter_logs.sort(key=lambda x: (x[1], x[0]))
        ret = [' '.join(letter_log) for letter_log in letter_logs] + digit_logs
        return ret

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

print(Solution.reorderLogFiles(Solution(), logs))
