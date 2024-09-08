from typing import List

# TLE on 17/32 testcases

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:

    def dist(x, y):
        d = abs(x - y)
        return min(d, N - d)

    def dp(i, j):
        if i == M:
            return 0
        
        if memo[i][j] != -1:
            return memo[i][j]
        
        p = rev_icm[j]

        dist1 = dist(p, C[i])
        dist2 = dist(C[i - 1], C[i])

        memo[i][j] = min(
            dist1 + dp(i + 1, icm[C[i - 1]]),
            dist2 + dp(i + 1, j),
        )
        return memo[i][j]

    # index compression map
    icm = {1: 0}
    rev_icm = [1]
    cur = 1
    for c in C:
        if c in icm:
            continue
        icm[c] = cur
        cur += 1
        rev_icm.append(c)

    memo = [[-1 for _ in range(cur - 1)] for _ in range(M)]

    return dist(1, C[0]) + dp(1, 0)


if __name__ == "__main__":

    N = 3
    M = 3
    C = [1, 2, 3]
    print(getMinCodeEntryTime(N, M, C), 2)

    N = 10
    M = 4
    C = [9, 4, 4, 8]
    print(getMinCodeEntryTime(N, M, C), 6)
