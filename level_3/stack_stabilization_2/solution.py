from typing import List
# Write any import statements here

def getMinimumSecondsRequired(N: int, R: List[int], A: int, B: int) -> int:
    # Write your code here
    ...

if __name__ == '__main__':

    N = 5
    R = [2, 5, 3, 6, 5]
    A = 1
    B = 1
    print(getMinimumSecondsRequired(N, R, A, B), 5)

    N = 3
    R = [100, 100, 100]
    A = 2
    B = 3
    print(getMinimumSecondsRequired(N, R, A, B), 5)

    N = 3
    R = [100, 100, 100]
    A = 7
    B = 3
    print(getMinimumSecondsRequired(N, R, A, B), 9)

    N = 4
    R = [6, 5, 4, 3]
    A = 10
    B = 1
    print(getMinimumSecondsRequired(N, R, A, B), 19)

    N = 4
    R = [100, 100, 1, 1]
    A = 2
    B = 1
    print(getMinimumSecondsRequired(N, R, A, B), 207)

    N = 6
    R = [6, 5, 2, 4, 4, 7]
    A = 1
    B = 1
    print(getMinimumSecondsRequired(N, R, A, B), 10)
