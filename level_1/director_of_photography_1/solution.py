# Write any import statements here
from functools import lru_cache

def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    # Write your code here

    @lru_cache(None)
    def dp(i, last, last_pos):
        if i == len(C) or i > last_pos + Y and last != '':
            return 0
        
        res = dp(i + 1, last, last_pos)
        if i < last_pos + X and last != '':
            return res
        if C[i] == 'P':
            if last == '':
                res += dp(i + 1, 'P', i)
            elif last == 'BA':
                res += 1
        elif C[i] == 'B':
            if last == '':
                res += dp(i + 1, 'B', i)
            elif last == 'PA':
                res += 1
        elif C[i] == 'A':
            if last == 'P':
                res += dp(i + 1, 'PA', i)
            elif last == 'B':
                res += dp(i + 1, 'BA', i)
        return res

    return dp(0, '', -1)



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
