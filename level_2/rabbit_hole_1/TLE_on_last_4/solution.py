from typing import List, Optional
# Write any import statements here

def getMaxVisitableWebpages(N: int, L: List[int]) -> int:
    # Write your code here
    def find_cycle(node: int) -> Optional[int]:
        turtoise = L[node]
        hare = L[L[node]]
        while turtoise != hare:
            if visited[turtoise]:
                return
            visited[turtoise] = True
            turtoise = L[turtoise]
            hare = L[L[hare]]
        return turtoise
        
    def mark_cycle(start: int) -> None:
        node = L[start]
        size = 1
        while node != start:
            visited[node] = True
            size += 1
            node = L[node]

        cycle_size[start] = size
        node = L[start]
        while node != start:
            cycle_size[node] = size
            node = L[node]


    L = [x - 1 for x in L]

    cycle_size = [1 for _ in range(N)]
    sources = {i for i in range(N)}
    visited = [False for _ in range(N)]
    for node in range(N):
        if L[node] in sources:
            sources.remove(L[node])
        if visited[node]:
            continue
        start = find_cycle(node)
        if start is not None:
            mark_cycle(start)
        
        visited[node] = True

    sol = max(cycle_size)
    for node in sources:
        cur = node
        cur_len = 0
        while cycle_size[cur] == 1:
            cur = L[cur]
            cur_len += 1
        cur_len += cycle_size[cur]
        sol = max(sol, cur_len)

    return sol


if __name__ == "__main__":
    L = [2,4,2,3,1,1,6]
    L = [4, 1, 2, 1]
    L = [2, 4, 2, 2, 3]
    L = [4, 3, 5, 1, 2]
    print(getMaxVisitableWebpages(len(L), L))