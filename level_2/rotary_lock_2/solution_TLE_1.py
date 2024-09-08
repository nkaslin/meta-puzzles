from typing import List
from functools import lru_cache

# TLE on 23/32 test cases


def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:

    @lru_cache(None)
    def dp(i, p):
        if i == M:
            return 0
        
        dist1 = min(abs(p - C[i]), N - abs(p - C[i]))
        dist2 = min(abs(C[i-1] - C[i]), N - abs(C[i-1] - C[i]))

        return min(
            dist1 + dp(i + 1, C[i-1]),
            dist2 + dp(i + 1, p),
        )
    
    return min(abs(1 - C[0]), N - abs(1 - C[0])) + dp(1, 1)


if __name__ == "__main__":

    N = 3
    M = 3
    C = [1, 2, 3]
    print(getMinCodeEntryTime(N, M, C), 2)

    N = 10
    M = 4
    C = [9, 4, 4, 8]
    print(getMinCodeEntryTime(N, M, C), 6)
