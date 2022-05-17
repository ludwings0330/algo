class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        letters = {"2":list("abc"), "3":list("def"), "4":list("ghi"),
                   "5":list("jkl"), "6":list("mno"), "7":list("pqrs"),
                   "8":list("tuv"), "9":list("wxyz")}

        import collections
        dq = collections.deque()
        for digit in digits:
            letter_list = letters[digit]
            if not dq:
                dq.append("")
            for _ in range(len(dq)):
                before = dq.popleft()
                for ch in letter_list:
                    dq.append(before + ch)

        return list(dq)

print(Solution().letterCombinations("23"))