from typing import List
# Write any import statements here

def getMinProblemCount(N: int, S: List[int]) -> int:
    # Write your code here
    for score in S:
        if score % 2 == 1:
            return max(S) // 2 + 1
    return max(S) // 2 

if __name__ == '__main__':

    N = 6
    S = [1, 2, 3, 4, 5, 6]
    print(getMinProblemCount(N, S))

    N = 4
    S = [4, 3, 3, 4]
    print(getMinProblemCount(N, S))
    
    N = 4
    S = [2, 4, 6, 8]
    print(getMinProblemCount(N, S))
