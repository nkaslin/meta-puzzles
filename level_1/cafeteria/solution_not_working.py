from typing import List
# Write any import statements here

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    # Write your code here
    arr = [1 - K] + sorted(S) + [N + K + 1]
    res = 0
    for x, y in zip(arr, arr[1:]):
        space = y - x - 1 - 2 * K
        if space > 0:
            res += (space + K) // (K + 1)
        
    return res