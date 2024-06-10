# Write any import statements here

def getWrongAnswers(N: int, C: str) -> str:
    # Write your code here
    return ''.join(['A' if x == 'B' else 'B' for x in C])