from typing import List, Tuple

import sys
sys.setrecursionlimit(10**6)


class Kosaraju:

    def __init__(self, graph: List[List[int]]):
        self.graph = graph

        self._n = len(graph)
        self._reverse_graph = [[] for _ in range(self._n)]
        self._create_reverse_graph()
        self._order = []
        self._visited = [False for _ in range(self._n)]
        self._groups = [-1 for _ in range(self._n)]
        self._cur_group = 0

        self._simplified_graph = None
        self._mappings = None


    def _create_reverse_graph(self) -> None:
        for x, neigh in enumerate(self.graph):
            for y in neigh:
                self._reverse_graph[y].append(x)

    def _perform_algo(self) -> None:
        
        # 1st phase of Kosaraju: dfs to construct last visited order
        for node in range(self._n):
            if self._visited[node]:
                continue
            self._dfs_1(node)

        # 2nd phase of Kosaraju: dfs on reverse graph to assign groups
        for node in self._order[::-1]:
            if self._groups[node] != -1:
                continue
            self._dfs_2(node)
            self._cur_group += 1

        # construct simplified graph and original node mappings
        self._mappings = [[] for _ in range(self._cur_group)]
        for node, group in enumerate(self._groups):
            self._mappings[group].append(node)
        self._simplified_graph = [set() for _ in range(self._cur_group)]
        
        self._simplify_graph()
        self._simplified_graph = [list(x) for x in self._simplified_graph]


    def _dfs_1(self, node: int) -> None:
        self._visited[node] = True
        for neigh in self.graph[node]:
            if self._visited[neigh]:
                continue
            self._dfs_1(neigh)
        self._order.append(node)        

    def _dfs_2(self, node: int) -> None:
        self._groups[node] = self._cur_group
        for neigh in self._reverse_graph[node]:
            if self._groups[neigh] != -1:
                continue
            self._dfs_2(neigh)

    def _simplify_graph(self) -> None:
        for group in range(self._cur_group):
            for x in self._mappings[group]:
                for y in self.graph[x]:
                    if self._groups[y] == group:
                        continue
                    self._simplified_graph[group].add(self._groups[y])

    def get_simplified_graph(self) -> Tuple[List[List[int]], List[List[int]], List[int]]:
        """
        returns the new, simplified graph and two mappings,
        the first mappings maps new nodes (index) to old nodes (list of nodes)
        the second mapping maps old nodes (index) to new nodes (integer value)
        """
        self._perform_algo()
        return (self._simplified_graph, self._mappings, self._groups)
    

class TopoSort:

    def __init__(self, graph: List[List[int]]):
        self.graph = graph

        self._n = len(self.graph)
        self._ordering = []
        self._processed = [False for _ in range(self._n)]

    def _perform_algo(self) -> None:
        for node in range(self._n):
            if self._processed[node]:
                continue
            self._dfs(node)
        
    def _dfs(self, node: int) -> None:
        self._processed[node] = True
        for neigh in self.graph[node]:
            if self._processed[neigh]:
                continue
            self._processed[neigh] = True
            self._dfs(neigh)
        self._ordering.append(node)

    def get_order(self) -> List[int]:
        self._perform_algo()
        return self._ordering[::-1]

def getMaxVisitableWebpages(N: int, M: int, A: List[int], B: List[int]) -> int:

    def dfs(node: int) -> int:
        if visited[node]:
            return max_len[node]
        visited[node] = True
        for neigh in simplified_graph[node]:
            max_len[node] = max(max_len[node], len(map_new_old[node]) + dfs(neigh))
        return max_len[node]

    
    graph = [[] for _ in range(N)]
    for a, b in zip(A, B):
        graph[a - 1].append(b - 1)

    kosaraju = Kosaraju(graph=graph)
    simplified_graph, map_new_old, _ = kosaraju.get_simplified_graph()

    toposort = TopoSort(graph=simplified_graph)
    order = toposort.get_order()

    res = 0
    max_len = [len(x) for x in map_new_old]
    visited = [False for _ in map_new_old]
    for node in order:
        res = max(res, dfs(node))

    return res


if __name__ == "__main__":

    N = 10
    M = 9
    A = [3, 2, 5, 9, 10, 3, 3, 9, 4]
    B = [9, 5, 7, 8, 6, 4, 5, 3, 9]
    
    print(getMaxVisitableWebpages(N, M, A, B))