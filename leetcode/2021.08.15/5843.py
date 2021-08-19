# title : number of String That Appear as Substring in word

patterns = ["a", "abc", "bc", "d"]
word = "abc"

ans = 0
for pattern in patterns:
    isAnswer = False

    len_pattern = len(pattern)
    for i in range(len(word)):
        if len_pattern + i <= len(word):
            if pattern == word[i:i+len_pattern]:
                ans += 1
                break
print(ans)