from structures.graph import Graph, GraphType, VertexState
from enum import Enum


class Colors(Enum):

    BLUE = 1
    RED = 2
    UNCOLORED = 3


class TwoColoringGraph(Graph):

    def process_edge_creation(self, u, v):
        if u not in self.colors:
            self.colors[u] = Colors.UNCOLORED


    def complement_color(self, color):
        if color is Colors.RED: return Colors.BLUE
        if color is Colors.BLUE: return Colors.RED

        return Colors.UNCOLORED


    def process_edge(self, u, v):
        if self.colors[u] == self.colors[v]:
            print('not a bipartite graph', u, self.colors[u], v, self.colors[v])

        self.colors[v] = self.complement_color(self.colors[u])
        


if __name__ == "__main__":
    g = TwoColoringGraph(GraphType.UNDIRECTED)

    # square graph
    g.insert_edges([
        (1, 2, 0), (2, 3, 0), (3, 4, 0), (1, 4, 0)
    ])

    for e in g.edges:
        if g.states[e] is VertexState.UNDISCOVERED:
            g.colors[e] = Colors.RED
            g.bfs(e)