from typing import List
# Write any import statements here
from collections import defaultdict, deque

def getSecondsRequired(R: int, C: int, G: List[List[str]]) -> int:
    # Write your code here

    portals = defaultdict(list)
    
    for i in range(R):
        for j in range(C):
            if 97 <= ord(G[i][j]) <= 97 + 26:
                portals[G[i][j]].append((i, j))
            if G[i][j] == 'S':
                start = (i, j)
    
    q = deque([(start, 0)])
    visited = set()
    
    while q:
        (x, y), dist = q.popleft()
        if G[x][y] == 'E':
            return dist
        if (x, y) in visited:
            continue
        visited.add((x, y))
        if 97 <= ord(G[x][y]) <= 97 + 26:
            for i, j in portals[G[x][y]]:
                if (i, j) not in visited:
                    q.append(((i, j), dist + 1))
        for i, j in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if 0 <= i < R and 0 <= j < C and G[i][j] != '#':
                if (i, j) not in visited:
                    q.append(((i, j), dist + 1))
    
    return -1
    

if __name__ == '__main__':
    R = 3
    C = 3
    G = [['.', 'E', '.'], ['.', '#', 'E'], ['.', 'S', '#']]
    print(getSecondsRequired(R, C, G))

    R = 3
    C = 4
    G = [['a', '.', 'S', 'a'], ['#', '#', '#', '#'], ['E', 'b', '.', 'b']]
    print(getSecondsRequired(R, C, G))

    R = 3
    C = 4
    G = [['a', 'S', '.', 'b'], ['#', '#', '#', '#'], ['E', 'b', '.', 'a']]
    print(getSecondsRequired(R, C, G))

    R = 1
    C = 9
    G = [['x', 'S', '.', '.', 'x', '.', '.', 'E', 'x']]
    print(getSecondsRequired(R, C, G))
