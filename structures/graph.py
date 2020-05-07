from enum import Enum

# class GraphNode:
    
#     def __init__(self, value = None, children = None):
#         self.value = value
#         self.children = children


class GraphType(Enum):

    DIRECTED = 1
    UNDIRECTED = 2


class Graph:

    def __init__(self, graph_type):
        self.type = graph_type
        self.edges = {}


    def insert_vertex(self, value):
        if value in self.edges:
            raise Exception('vertex with value {value} already exists. bailing')

        self.edges[value] = []


    def insert_edge(self, i, j, graph_type = None):
        if graph_type is None:
            graph_type = self.type

        if i in self.edges:
            self.edges[i].append(j)
        else:
            self.edges[i] = [j]

        if graph_type is GraphType.UNDIRECTED:
            self.insert_edge(j, i, GraphType.DIRECTED)


class VertexState(Enum):

    UNDISCOVERED = 1
    DISCOVERED = 2
    PROCESSED = 3


def bfs(graph, root):
    states = {}
    parents = {}
    
    for e in graph.edges:
        states[e] = VertexState.UNDISCOVERED
        parents[e] = None

    states[root] = VertexState.DISCOVERED
    q = [root]

    while len(q) != 0:
        u = q.pop()

        # vertex_processor(u)

        for v in graph.edges[u]:
            # edge_processor(u, v)
            print("now processing edge u", u, "v", v)
            
            if states[v] == VertexState.UNDISCOVERED:
                states[v] = VertexState.DISCOVERED
                q.insert(0, v)
                parents[v] = u

        states[u] = VertexState.PROCESSED


if __name__ == "__main__":
    g = Graph(GraphType.UNDIRECTED)

    g.insert_edge(1, 2)
    g.insert_edge(1, 5)
    g.insert_edge(5, 2)
    g.insert_edge(5, 4)
    g.insert_edge(2, 4)
    g.insert_edge(2, 3)

    bfs(g, 1)

    # for vertex, outedges in g.edges.items():
    #     print("v", vertex, "edges", str(outedges))

    