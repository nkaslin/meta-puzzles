
Graph = list[list[int]]

class Kosaraju:

    def __init__(self, graph: Graph):
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

    def get_simplified_graph(self) -> tuple[Graph, list[list[int]], list[int]]:
        """
        returns the new, simplified graph and two mappings,
        the first mappings maps new nodes (index) to old nodes (list of nodes)
        the second mapping maps old nodes (index) to new nodes (integer value)
        """
        self._perform_algo()
        return (self._simplified_graph, self._mappings, self._groups)


if __name__ == "__main__":

    g = [[1, 3], [0, 4], [1, 6], [], [3], [2, 4], [5]]
    
    algo = Kosaraju(graph=g)
    simplified_graph, map_new_old, map_old_new = algo.get_simplified_graph()

    print(simplified_graph)
    print(map_new_old)
    print(map_old_new)
