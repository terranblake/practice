from structures.graph import Graph, GraphType


class TwoColoringGraph(Graph):

    def process_edge(self, u, v):
        print('processing edge =>', u, v)


if __name__ == "__main__":
    g = TwoColoringGraph(GraphType.UNDIRECTED)

    # component #1
    component_1_edges = [
        (1, 2), (1, 5), (5, 2), (5, 4), (2, 4),
        (2, 3), (4, 6), (6, 10), (6, 11), (6, 8),
        (6, 7), (10, 11), (6, 10), (7, 8), (8, 9)
    ]

    for edge in component_1_edges:
        g.insert_edge(edge[0], edge[1])
    
    # component #2
    component_2_edges = [
        (16, 12), (16, 13), (16, 14), (16, 15),
        (16, 17), (12, 13), (13, 14), (14, 15),
        (15, 17), (17, 12)
    ]

    for edge in component_2_edges:
        g.insert_edge(edge[0], edge[1])

    # do a bfs
    print(g.edges)
    parents = g.bfs(1)