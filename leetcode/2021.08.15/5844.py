# title : Minimum Non-Zero Product of the Array Elements

def solution(p):
    # p 개의 bit 켠다
    # [1, 2^p -1]
    MOD = 10**9 + 7
    ans = (2**p -1) % MOD
    if p == 1:
        return 1
    elif p == 2:
        return 6
    else:
        k = ((1 << p) - 1) ^ 1
        ans = (ans * (k ** (2**(p-1) -1) )) % MOD
        return ans
print(solution(60))
