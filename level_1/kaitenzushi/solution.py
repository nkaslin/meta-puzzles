from typing import List
# Write any import statements here
from collections import deque

def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
    # Write your code here
    eaten_dishes = deque([(D[0], 0)])
    blocked_dishes = {D[0]}
    res = 1
    for i in range(1, N):
        if len(eaten_dishes) > K:
            blocked_dishes.remove(eaten_dishes.popleft()[0])
        if D[i] not in blocked_dishes:
            eaten_dishes.append((D[i], i))
            blocked_dishes.add(D[i])
            res += 1
    return res 


if __name__ == '__main__':

    N = 6
    D = [1, 2, 3, 3, 2, 1]
    K = 1
    print(getMaximumEatenDishCount(N, D, K))

    N = 6
    D = [1, 2, 3, 3, 2, 1]
    K = 2
    print(getMaximumEatenDishCount(N, D, K))
    
    N = 7
    D = [1, 2, 1, 2, 1, 2, 1]
    K = 2
    print(getMaximumEatenDishCount(N, D, K))
