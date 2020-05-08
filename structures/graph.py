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

        self.finished = False
        self.state = {}
        self.parents = {}

        self.time = 0
        self.entry_time = {}
        self.exit_time = {}


    def insert_edge(self, i, j, graph_type = None):
        if graph_type is None:
            graph_type = self.type

        if i not in self.edges:
            self.edges[i] = []

        edge = EdgeNode(j, None, self.edges[i])
        self.edges[i].append(edge)

        if graph_type is GraphType.UNDIRECTED:
            self.insert_edge(j, i, GraphType.DIRECTED)


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
        '''
        pass


    def bfs(self, root = 1):
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
                self.process_edge(u, v.value)

                # we need to search this vertex for more edges
                if states[v.value] == VertexState.UNDISCOVERED:
                    # we've touched this edge but haven't explored it's edges
                    states[v.value] = VertexState.DISCOVERED

                    # insert this vertex at the beginning of the queue
                    q.insert(0, v.value)

                    # set the parent for this vertex
                    parents[v.value] = u

            # end processing this vertex
            states[u] = VertexState.PROCESSED

            self.process_vertex_late(u)
        
        # return the parent mappings to the caller
        return parents


    def dfs(self, root):
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
                self.process_edge(u, v.value)

                # we need to search this vertex for more edges
                if states[v.value] == VertexState.UNDISCOVERED:
                    # we've touched this edge but haven't explored it's edges
                    states[v.value] = VertexState.DISCOVERED

                    # insert this vertex at the beginning of the queue
                    q.append(v.value)

                    # set the parent for this vertex
                    parents[v.value] = u

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


if __name__ == "__main__":
    g = Graph(GraphType.UNDIRECTED)

    # component #1
    component_1_edges = [
        (1, 2), (1, 5), (5, 2), (5, 4), (2, 4),
        (2, 3), (4, 6), (6, 10), (6, 11), (6, 8),
        (6, 7), (10, 11), (6, 10), (7, 8), (8, 9)
    ]

    for edge in component_1_edges:
        g.insert_edge(edge[0], edge[1])

    # do a bfs
    # parents = g.bfs(1)

    # do a dfs
    parents = g.dfs(1)

    # get a path from one node to another
    # print(g.find_path(3, 1))