from typing import List
# Write any import statements here

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
    # Write your code here
    last = 1
    res = 0
    for x in C:
        res += min(abs(last - x), N - abs(last - x))
        last = x
    return res

if __name__ == "__main__":
    N = 10
    M = 4
    C = [9, 4, 4, 8]
    print(getMinCodeEntryTime(N, M, C))