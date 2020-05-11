from structures.graph import Graph, GraphType
from enum import Enum


class Colors(Enum):

    BLUE = 1
    GREEN = 2
    RED = 3


class TwoColoringGraph(Graph):

    def process_edge_creation(self, u, v):
        if u not in self.colors:
            self.colors[u] = None


    def process_edge(self, u, v):
        if self.colors[u] is None:
            self.colors[u] = Colors.RED

        color = self.colors[u]
        if self.colors[v] is None:
            if color is Colors.RED:
                self.colors[v] = Colors.GREEN
            elif color is Colors.GREEN:
                self.colors[v] = Colors.BLUE
            else:
                print('not a valid 3-color graph')

        print(v, self.colors[v])
        


if __name__ == "__main__":
    g = TwoColoringGraph(GraphType.UNDIRECTED)

    # peterson graph
    peterson_graph_edges = [
        (1, 2, 0), (1, 3, 0), (1, 5, 0), (2, 8, 0), (2, 7, 0),
        (5, 6, 0), (5, 10, 0), (10, 7, 0), (10, 9, 0), (9, 8, 0),
        (3, 4, 0), (3, 9, 0), (7, 4, 0), (8, 6, 0), (6, 4, 0)
    ]

    g.insert_edges(peterson_graph_edges)

    # do a bfs
    g.bfs(1)