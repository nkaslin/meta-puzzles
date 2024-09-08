from typing import List


def getSecondsElapsed(C: int, N: int, A: List[int], B: List[int], K: int) -> int:

    tunnels = sorted([(a, b) for a, b in zip(A, B)])
    res, rem = divmod(K, sum(b - a for a, b in tunnels))
    res *= C

    if rem == 0:
        return res - C + tunnels[-1][1]

    ptr = 0
    while rem > 0:
        rem -= tunnels[ptr][1] - tunnels[ptr][0]
        ptr += 1

    return res + tunnels[ptr - 1][1] + rem


if __name__ == "__main__":

    C = 10
    N = 2
    A = [1, 6]
    B = [3, 7]
    K = 7
    print(getSecondsElapsed(C, N, A, B, K), 22)

    C = 50
    N = 3
    A = [39, 19, 28]
    B = [49, 27, 35]
    K = 15
    print(getSecondsElapsed(C, N, A, B, K), 35)

    C = 10
    N = 1
    A = [1]
    B = [6]
    K = 15
    print(getSecondsElapsed(C, N, A, B, K), 26)
