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
    # stores the current state of each vertex
    states = {}

    # stores the parent for a given vertex, by value
    # e.g. vertex id 5 's parent is stored at parents[5]
    parents = {}
    
    # set all edges to undiscovered and parents to unset
    for e in graph.edges:
        states[e] = VertexState.UNDISCOVERED
        parents[e] = None

    # set the root vertex to discovered
    states[root] = VertexState.DISCOVERED

    # init the queue with the root element
    q = [root]

    while len(q) != 0:
        # get the vertex from the queue
        u = q.pop()

        # iterate through each outedge for the current vertex
        for v in graph.edges[u]:

            # we need to search this vertex for more edges
            if states[v] == VertexState.UNDISCOVERED:
                
                # we've touched this edge but haven't explored it's edges
                states[v] = VertexState.DISCOVERED

                # insert this vertex at the beginning of the queue
                q.insert(0, v)

                # set the parent for this vertex
                parents[v] = u

        # end processing this vertex
        states[u] = VertexState.PROCESSED


def dfs(graph, root):
    pass


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

    