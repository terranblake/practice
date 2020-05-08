from enum import Enum


class VertexState(Enum):

    UNDISCOVERED = 1
    DISCOVERED = 2
    PROCESSED = 3


class GraphType(Enum):

    DIRECTED = 1
    UNDIRECTED = 2


class Graph(object):

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


    def process_vertex_early(self, v):
        pass


    def process_edge(self, u, v):
        pass


    def process_vertex_late(self, v):
        pass


    def bfs(self, root):
        '''
        Does a breadth-first search on the provided graph, starting from the 
        provided root, then returns the parent associations for the vertices touched
        '''

        # stores the current state of each vertex
        states = {}

        # stores the parent for a given vertex, by value
        # e.g. vertex id 5 's parent is stored at parents[5]
        parents = {}
        
        # set all edges to undiscovered and parents to unset
        for e in self.edges:
            states[e] = VertexState.UNDISCOVERED

        # set the root vertex to discovered
        states[root] = VertexState.DISCOVERED

        # init the queue with the root element
        q = [root]

        while len(q) != 0:
            # get the vertex from the queue
            u = q.pop()

            self.process_vertex_early(u)

            # iterate through each outedge for the current vertex
            for v in self.edges[u]:
                self.process_edge(u, v)

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

            self.process_vertex_late(u)
        
        # return the parent mappings to the caller
        return parents


    def find_path(self, i, j):
        '''
        Finds a path between to vertices in the graph
        i should be further up the graph (closer to the root) than j

        Since graphs can have multiple components (distinctly separate parts),
        we use the origin of the path to do a bfs prior to finding the path
        to avoid a scenario where a previous bfs didn't discover a disconnected
        set of edges
        '''

        parents = self.bfs(i)

        path = [j]
        current = j
        while current is not None and current != i:
            if current not in parents:
                return False

            current = parents[current]
            path.insert(0, current)

        return path


    def find_components(self):
        '''
        Does a bfs for each separate component of the graph
        returning a node for each component that was discovered
        '''
        discovered = []
        components = []

        for u in self.edges:
            if u not in discovered:
                components.append(u)
                
                found = self.bfs(u)
                for x in found:
                    discovered.append(x)

        return components


    def dfs(self, root):
        pass