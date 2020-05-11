from structures.graph import Graph, GraphType


if __name__ == "__main__":
    g = Graph(GraphType.UNDIRECTED)

    edges = [
        (0, 1, 0), (0, 2, 0), (1, 3, 0),
        (1, 4, 0), (4, 6, 0), (2, 5, 0), (5, 7, 0)
    ]

    g.insert_edges(edges)
    g.dfs(0)

    # print(g.is_ancestor(1, 6))
    # print(g.is_ancestor(1, 7))
    # print(g.is_ancestor(3, 4))
    # print(g.is_ancestor(0, 7))

    # print(g.count_descendants(0))
    # print(g.count_descendants(1))
    # print(g.count_descendants(7))