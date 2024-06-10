# Write any import statements here

def getUniformIntegerCountInInterval(A: int, B: int) -> int:
    # Write your code here
    lA, lB = len(str(A)), len(str(B))
    res = int(int(str(A)[0] * lA) >= A)
    res += 9 - int(str(A)[0])
    res += (lB - lA - 1) * 9
    res += int(str(B)[0])
    res -= int(int(str(B)[0] * lB) > B)
    return res

if __name__ == '__main__':

    A = 75
    B = 300
    print(getUniformIntegerCountInInterval(A, B))

    A = 1
    B = 9
    print(getUniformIntegerCountInInterval(A, B))

    A = 999999999999
    B = 999999999999
    print(getUniformIntegerCountInInterval(A, B))
