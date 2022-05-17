class Solution:
    def combinationSum(self, candidates: list[int],target: int) -> list[list[int]]:
        result = []
        def dfs(index, score, board):
            if score == target:
                result.append(board.copy())
                return
            elif index == len(candidates) or score > target:
                return


            # 현재꺼 스킵
            dfs(index + 1, score, board)

            # 현재꺼 포함
            while score <= target:
                score += candidates[index]
                board = board + [candidates[index]]
                if score > target:
                    break

                dfs(index + 1, score, board)


        dfs(0, 0, [])

        return result

candidates = [2, 3, 6, 7]
target = 7

print(Solution().combinationSum(candidates, target))