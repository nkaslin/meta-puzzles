
Graph = list[list[int]]

class TopoSort:

    def __init__(self, graph: Graph):
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

    def get_order(self) -> list[int]:
        self._perform_algo()
        return self._ordering[::-1]

if __name__ == "__main__":

    g = [[1], [2], [5], [0, 4], [1, 2], []]
    
    algo = TopoSort(graph=g)
    print(algo.get_order())
    