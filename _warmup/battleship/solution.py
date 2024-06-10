from typing import List
# Write any import statements here

def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:
    # Write your code here
    return sum(sum(x) for x in G) / (R * C)