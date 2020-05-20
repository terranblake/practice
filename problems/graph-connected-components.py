from structures.graph import Graph, GraphType, VertexState, EdgeType


class ConnectedComponentsGraph(Graph):

    def find_components(self):
        '''
        Does a bfs for each separate component of the graph
        returning a node for each component that was discovered
        '''
        components = []

        for u in self.edges.keys():
            if self.states[u] == VertexState.UNDISCOVERED:
                components.append(u)
                self.bfs(u)

        return components


if __name__ == "__main__":
    g = ConnectedComponentsGraph(GraphType.UNDIRECTED)

    g.insert_edges([
        (1, 2, 0), (1, 8, 0), (1, 3, 0),
        (2, 4, 0), (4, 6, 0), (6, 2, 0),
        (3, 5, 0), (5, 4, 0), (5, 7, 0),
        (5, 8, 0)
    ])

    g.insert_edges([(10, 11, 0)])

    print(g.find_components())