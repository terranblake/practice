from structures.graph import Graph, GraphType


class EdgeClassificationGraph(Graph):

    def process_edge(self, u, v):
        print(u, self.states[u], v, self.parents[v])

        if self.parents[v] != u:
            # self.parents[v] = u
            print((u, v), 'back edge detected', self.find_path(u, v))
            self.finished = True



if __name__ == "__main__":
    g = EdgeClassificationGraph(GraphType.DIRECTED)

    # component with all types of edges
    # component_1_edges = [
    #     (1, 8), (1, 3), (1, 2), (2, 4), (4, 6), (6, 2), (3, 5), (5, 4), (5, 7), (5, 8)
    # ]

    # component with only a back edge
    component = [
        (1, 6), (1, 2), (2, 3), (3, 4), (4, 5), (5, 2), (5, 1)
    ]

    for edge in component:
        g.insert_edge(edge[0], edge[1], None)

    g.dfs(1)