from typing import List
# Write any import statements here

def getMinimumDeflatedDiscCount(N: int, R: List[int]) -> int:
    # Write your code here
    res = 0
    last = float('inf')
    for disk in R[::-1]:
        if disk < last:
            last = disk
            continue
        res += 1
        last -= 1
    if last < 1:
        return -1
    return res


if __name__ == '__main__':

    N = 5
    R = [2, 5, 3, 6, 5]
    print(getMinimumDeflatedDiscCount(N, R))

    N = 3
    R = [100, 100, 100]
    print(getMinimumDeflatedDiscCount(N, R))

    N = 4
    R = [6, 5, 4, 3]
    print(getMinimumDeflatedDiscCount(N, R))
    