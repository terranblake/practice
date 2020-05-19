from structures.graph import Graph, GraphType


class TopologicalSortGraph(Graph):
    def process_vertex_late(self, u):
        self.topsort.insert(0, u)


if __name__ == "__main__":
    g = TopologicalSortGraph(GraphType.DIRECTED)
    g.topsort = []

    edges = [
        ('G', 'A', 0), ('G', 'F', 0), ('A', 'C', 0),
        ('A', 'B', 0), ('B', 'C', 0), ('C', 'F', 0),
        ('F', 'E', 0), ('E', 'D', 0), ('B', 'D', 0)
    ]
    g.insert_edges(edges)

    g.dfs('G')

    print(g.topsort)