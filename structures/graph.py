from enum import Enum


class VertexState(Enum):

    UNDISCOVERED = 1
    DISCOVERED = 2
    PROCESSED = 3


class TraversalType(Enum):

    DFS = 1
    BFS = 2


class GraphType(Enum):

    DIRECTED = 1
    UNDIRECTED = 2


class EdgeNode(object):

    def __init__(self, value, weight, next):
        self.value = value
        self.weight = weight
        self.next = next

    
    def stringify(self):
        return "value {0} weight {1} next {2}".format(self.value, self.weight, self.next)


class Graph(object):

    def __init__(self, graph_type):
        self.type = graph_type
        self.edges = {}

        # used for quitting anything early
        self.finished = False

        self.time = 0

        # the time that this edge was discovered
        self.entry_time = {}

        # the time that this edge was processed
        self.exit_time = {}

        # stores the current state of each vertex
        self.states = {}

        # stores the parent for a given vertex, by value
        # e.g. vertex id 5 's parent is stored at parents[5]
        self.parents = {}


    def insert_edge(self, i, j, weight, graph_type = None):
        if graph_type is None:
            graph_type = self.type

        if i not in self.edges:
            self.edges[i] = []
            self.states[i] = VertexState.UNDISCOVERED
            self.parents[i] = None

        if j not in self.states:
            self.states[j] = VertexState.UNDISCOVERED
            self.parents[j] = None

        if j not in self.edges:
            self.edges[j] = []

        edge = EdgeNode(j, weight, self.edges[i])
        self.edges[i].append(edge)

        if graph_type is GraphType.UNDIRECTED:
            self.insert_edge(j, i, weight, GraphType.DIRECTED)


    def process_vertex_early(self, v):
        '''
        Called when the vertex is remove from the queue/stack, but before processing
        all associated edges related to this vertex
        '''
        # print(v)


    def process_edge(self, u, v):
        '''
        Called the very first time the vertex u is found, just before being added to the
        stack/queue. Vertex u will be processed again once removed from the container
        '''
        pass


    def process_vertex_late(self, v):
        '''
        Called after all of the edges related to this vertex have been added to the queue
        or when the vertex has been set to PROCESSED
        '''
        pass

    def bfs(self, root = 1):
        '''
        Does a breadth-first search on the provided graph, starting from the 
        provided root, then returns the parent associations for the vertices touched
        '''
        
        # set all edges to undiscovered and parents to unset
        for e in self.edges:
            self.states[e] = VertexState.UNDISCOVERED

        # set the root vertex to discovered
        self.states[root] = VertexState.DISCOVERED

        # init the queue with the root element
        q = [root]

        while len(q) != 0:
            # get the vertex from the queue
            u = q.pop()

            self.process_vertex_early(u)

            # iterate through each outedge for the current vertex
            for v in self.edges[u]:
                self.process_edge(u, v.value)

                # we need to search this vertex for more edges
                if self.states[v.value] == VertexState.UNDISCOVERED:
                    # we've touched this edge but haven't explored it's edges
                    self.states[v.value] = VertexState.DISCOVERED

                    # insert this vertex at the beginning of the queue
                    q.insert(0, v.value)

                    # set the parent for this vertex
                    self.parents[v.value] = u

            # end processing this vertex
            self.states[u] = VertexState.PROCESSED

            self.process_vertex_late(u)
        
        # return the parent mappings to the caller
        return self.parents


    def dfs(self, root):
        '''
        Does a breadth-first search on the provided graph, starting from the 
        provided root, then returns the parent associations for the vertices touched
        '''
        
        # set all edges to undiscovered and parents to unset
        for e in self.edges:
            self.states[e] = VertexState.UNDISCOVERED

        # set the root vertex to discovered
        self.states[root] = VertexState.DISCOVERED

        # init the queue with the root element
        q = [root]

        while len(q) != 0:
            # get the vertex from the queue
            u = q.pop()

            self.process_vertex_early(u)

            # iterate through each outedge for the current vertex
            for v in self.edges[u]:

                if self.finished is True: break

                if self.states[v.value] == VertexState.UNDISCOVERED:
                    self.parents[v.value] = u
                    self.process_edge(u, v.value)
                    self.states[v.value] = VertexState.DISCOVERED
                    q.append(v.value)

                # once processed, we need to check the edge type
                if self.states[v.value] == VertexState.PROCESSED:
                    self.process_edge(u, v.value)

            # end processing this vertex
            self.states[u] = VertexState.PROCESSED

            self.process_vertex_late(u)

            # print(u, v.value, self.states[v.value])
        
        # return the parent mappings to the caller
        return self.parents


    def find_path(self, i, j):
        '''
        Finds a path between to vertices in the graph
        i should be further up the graph (closer to the root) than j

        Since graphs can have multiple components (distinctly separate parts),
        we use the origin of the path to do a bfs prior to finding the path
        to avoid a scenario where a previous bfs didn't discover a disconnected
        set of edges
        '''

        # make sure to run bfs before finding a path
        # TODO: this should be removed and flag that throws
        #       and error would sit in place of a graph not being
        #       traversed prior to finding a path

        path = [j]
        current = j
        while current is not None and current != i:
            if current not in self.parents:
                return False

            print(current, self.parents[current])

            current = self.parents[current]
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


if __name__ == "__main__":
    g = Graph(GraphType.UNDIRECTED)

    # component #1
    component_1_edges = [
        (1, 2), (1, 5), (5, 2), (5, 4), (2, 4),
        (2, 3), (4, 6), (6, 10), (6, 11), (6, 8),
        (6, 7), (10, 11), (6, 10), (7, 8), (8, 9)
    ]

    # unweighted graph edges
    for edge in component_1_edges:
        g.insert_edge(edge[0], edge[1], None)

    # do a bfs
    parents = g.bfs(1)

    # # do a dfs
    # parents = g.dfs(1)

    # get a path from one node to another
    print(g.find_path(1, 7))