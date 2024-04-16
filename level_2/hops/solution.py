from typing import List
# Write any import statements here

def getSecondsRequired(N: int, F: int, P: List[int]) -> int:
    # Write your code here
    return N - min(P)