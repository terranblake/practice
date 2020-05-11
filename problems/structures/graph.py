from enum import Enum


class VertexState(Enum):

    UNDISCOVERED = 1
    DISCOVERED = 2
    PROCESSED = 3


class EdgeType(Enum):

    TREE = 1    # parent is the node just above it
    BACK = 2    # points to a node which already has a parent
    BRIDGE = 3  # points to a node which has already been discovered


class GraphType(Enum):

    DIRECTED = 1
    UNDIRECTED = 2


class EdgeNode(object):

    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight

    
    def stringify(self):
        return "u {0} v {1} weight {2}".format(self.u, self.v, self.weight)


class Graph(object):

    def __init__(self, graph_type):
        self.type = graph_type
        self.edges = {}

        self.colors = {}
        self.types = {}

        # used for quitting anything early
        self.finished = False

        # global timer to track entry/exit times of vertices
        self.time = 0

        # the time that this edge was discovered
        self.entry_time = {}

        # the time that this edge was processed
        self.exit_time = {}

        # stores the current state of each vertex
        self.states = {}

        # stores the parent for a given vertex
        self.parents = {}


    def insert_edge(self, u, v, weight, graph_type = None):
        if graph_type is None:
            graph_type = self.type

        if u not in self.edges:
            self.edges[u] = []
            self.states[u] = VertexState.UNDISCOVERED
            self.parents[u] = None

        if v not in self.states:
            self.states[v] = VertexState.UNDISCOVERED
            self.parents[v] = None

        if v not in self.edges:
            self.edges[v] = []

        edge = EdgeNode(u, v, weight)
        self.edges[u].append(edge)

        self.process_edge_creation(u, v)

        if graph_type is GraphType.UNDIRECTED:
            self.insert_edge(v, u, weight, GraphType.DIRECTED)


    def insert_edges(self, edges):
        for [u, v, weight] in edges:
            self.insert_edge(u, v, weight)


    def process_edge_creation(self, u, v):
        '''
        Called when a new edge is created
        '''
        pass


    def count_descendants(self, u):
        '''
        Returns the count of descendant nodes for u by getting the entry and exit times
        for u and int dividing by 2. This would be the same as loop through all edges 
        and comparing the entry and exit times to the given vertex entry and exit times
        '''
        return (self.exit_time[u] - self.entry_time[u]) // 2


    def is_ancestor(self, u, v):
        '''
        Returns True if v is an ancestor of u
        '''
        if u not in self.entry_time or u not in self.exit_time:
            return None

        if v not in self.entry_time or v not in self.exit_time:
            return None

        started_before = self.entry_time[u] < self.entry_time[v]
        exited_after = self.exit_time[u] > self.exit_time[v]

        if started_before and exited_after:
            return True

        return False


    def edge_classification(self, u, v):
        # tree if u is parent
        if self.parents[v] == u:
            return EdgeType.TREE
        # bridge if v already has end time
        elif v in self.exit_time:
            return EdgeType.BRIDGE
        # back if v parent is not u
        elif self.parents[v] != u:
            return EdgeType.BACK


    def process_vertex_early(self, v):
        '''
        Called when the vertex is remove from the queue/stack, but before processing
        all associated edges related to this vertex
        '''
        pass


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
        breadth-first search
        '''
        
        # set all edges to undiscovered
        for u in self.edges:
            self.states[u] = VertexState.UNDISCOVERED

        # set the root vertex to discovered
        self.states[root] = VertexState.DISCOVERED

        # init the queue with the root element
        q = [root]

        while len(q) != 0:
            # get the vertex from the queue
            u = q.pop()

            self.process_vertex_early(u)

            # iterate through each outedge for the current vertex
            for e in self.edges[u]:
                self.process_edge(u, e.v)

                # we need to search this vertex for more edges
                if self.states[e.v] == VertexState.UNDISCOVERED:
                    # we've touched this edge but haven't explored it's edges
                    self.states[e.v] = VertexState.DISCOVERED

                    # insert this vertex at the beginning of the queue
                    q.insert(0, e.v)

                    # set the parent for this vertex
                    self.parents[e.v] = u

            # end processing this vertex
            self.states[u] = VertexState.PROCESSED

            self.process_vertex_late(u)


    def dfs(self, u = None):
        '''
        depth-first search
        '''

        self.time += 1

        # just before descendents are processed
        self.entry_time[u] = self.time

        self.states[u] = VertexState.DISCOVERED
    
        # before outedges are processed
        self.process_vertex_early(u)

        for e in self.edges[u]:
            state = self.states[e.v]
            self.process_edge(u, e.v)

            if state is VertexState.UNDISCOVERED:
                self.states[e.v] = VertexState.DISCOVERED
                self.parents[e.v] = u

                # edge_type = self.edge_classification(u, e.v)
                # just before edge from u to newly discovered edge is processed

                self.dfs(e.v)
        
        self.time += 1

        # all descendents have been processed
        self.exit_time[u] = self.time

        # after outedges are processed
        self.process_vertex_late(u)


    def find_path(self, i, j):
        '''
        Finds a path between to vertices in the graph
        '''

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
        (1, 2, 0), (1, 8, 0), (1, 3, 0),
        (2, 4, 0), (4, 6, 0), (6, 2, 0),
        (3, 5, 0), (5, 4, 0), (5, 7, 0),
        (5, 8, 0)
    ]

    # unweighted graph edges
    for edge in component_1_edges:
        g.insert_edge(edge[0], edge[1], edge[2])

    # do a bfs
    g.bfs(1)

    # # do a dfs
    # g.dfs(1)

    # print(g.parents)

    # get a path from one node to another
    print(g.find_path(6, 2))