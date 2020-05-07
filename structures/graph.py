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


if __name__ == "__main__":
    g = Graph(GraphType.UNDIRECTED)

    g.insert_edge(1, 2)
    g.insert_edge(1, 5)
    g.insert_edge(5, 2)
    g.insert_edge(5, 4)
    g.insert_edge(2, 4)
    g.insert_edge(2, 3)

    for vertex, outedges in g.edges.items():
        print("v", vertex, "edges", str(outedges))