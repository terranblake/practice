from enum import Enum
from graph import Graph, GraphType


class VertexState(Enum):

    UNDISCOVERED = 1
    DISCOVERED = 2
    PROCESSED = 3


def bfs(graph, root):
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
    for e in graph.edges:
        states[e] = VertexState.UNDISCOVERED

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
    
    # return the parent mappings to the caller
    return parents


def find_path(g, i, j):
    '''
    Finds a path between to vertices in the graph
    i should be further up the graph (closer to the root) than j

    Since graphs can have multiple components (distinctly separate parts),
    we use the origin of the path to do a bfs prior to finding the path
    to avoid a scenario where a previous bfs didn't discover a disconnected
    set of edges
    '''

    parents = bfs(g, i)

    path = [j]
    current = j
    while current is not None and current != i:
        if current not in parents:
            return False

        current = parents[current]
        path.insert(0, current)

    return path


def find_components(g):
    '''
    Does a bfs for each separate component of the graph
    returning a node for each component that was discovered
    '''
    discovered = []
    components = []

    for u in g.edges:
        if u not in discovered:
            components.append(u)
            
            found = bfs(g, u)
            for x in found:
                discovered.append(x)

    return components


def dfs(graph, root):
    pass


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
    
    # component #2
    component_2_edges = [
        (16, 12), (16, 13), (16, 14), (16, 15),
        (16, 17), (12, 13), (13, 14), (14, 15),
        (15, 17), (17, 12)
    ]

    for edge in component_2_edges:
        g.insert_edge(edge[0], edge[1])

    # do a bfs
    # parents = bfs(g, 1)

    # find the paht between 2 vertices
    path = find_path(g, 1, 10)
    print(path)

    # throws an error since these vertices are not connected
    path = find_path(g, 1, 16)
    print(path)

    # get a vertex from each component
    components = find_components(g)
    print(components)