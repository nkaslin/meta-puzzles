# Write any import statements here
from itertools import accumulate

def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    # Write your code here

    l = [c for c in C]
    B_pre = list(accumulate(l, lambda sm, x: sm + int(x == 'B'), initial=0))
    P_pre = list(accumulate(l, lambda sm, x: sm + int(x == 'P'), initial=0))
    

    AnextB = [0 for _ in range(N)]
    AnextP = [0 for _ in range(N)]
    for i, c in enumerate(l):
        if c != 'A': continue
        AnextB[i] = B_pre[min(len(B_pre)-1, i + Y + 1)] - B_pre[min(len(B_pre)-1, i + X)]
        AnextP[i] = P_pre[min(len(P_pre)-1, i + Y + 1)] - P_pre[min(len(P_pre)-1, i + X)]

    AnextB_pre = list(accumulate(AnextB, initial=0))
    AnextP_pre = list(accumulate(AnextP, initial=0))

    res = 0
    for i, c in enumerate(l):
        if c == 'B':
            res += AnextP_pre[min(len(B_pre)-1, i + Y + 1)] - AnextP_pre[min(len(B_pre)-1, i + X)]
        elif c == 'P':
            res += AnextB_pre[min(len(B_pre)-1, i + Y + 1)] - AnextB_pre[min(len(B_pre)-1, i + X)]

    return res
    


if __name__ == '__main__':

    N = 5
    C = 'APABA'
    X = 1
    Y = 2
    print(getArtisticPhotographCount(N, C, X, Y))

    N = 5
    C = 'APABA'
    X = 2
    Y = 3
    print(getArtisticPhotographCount(N, C, X, Y))

    N = 8
    C = '.PBAAP.B'
    X = 1
    Y = 3
    print(getArtisticPhotographCount(N, C, X, Y))
