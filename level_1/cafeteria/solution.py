from typing import List
# Write any import statements here

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    # Write your code here
    S.sort()
    res = 0
    left = 1
    for x in S + [N + K + 1]:
        right = x - K - 1
        res += 1 + (right - left) // (K + 1)
        left = x + K + 1
    return res


if __name__ == '__main__':

    N = 10
    K = 1
    M = 2
    S = [2, 6]
    print(getMaxAdditionalDinersCount(N, K, M, S), 3)

    N = 15
    K = 2
    M = 3
    S = [11, 6, 14]
    print(getMaxAdditionalDinersCount(N, K, M, S), 1)
