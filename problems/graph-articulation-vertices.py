from structures.graph import Graph, GraphType, VertexState, EdgeType
from enum import Enum


class ArticulationGraph(Graph):

    def process_edge_creation(self, u, v):
        self.tree_out_degree[u] = 0


    def process_vertex_early(self, u):
        self.reachable_ancestor[u] = u


    def edge_classification(self, u, v):
        if self.parents[v] == u:
            return EdgeType.TREE
        elif self.states[v] is VertexState.DISCOVERED:
            return EdgeType.BACK
        elif self.states[v] is VertexState.DISCOVERED and self.entry_time[v] > self.entry_time[u]:
            return EdgeType.FORWARD
        elif self.states[v] is VertexState.DISCOVERED and self.entry_time[v] < self.entry_time[u]:
            return EdgeType.CROSS


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

            if state is VertexState.UNDISCOVERED:
                self.states[e.v] = VertexState.DISCOVERED
                self.parents[e.v] = u

                self.process_edge(u, e.v)

                # edge_type = self.edge_classification(u, e.v)
                # just before edge from u to newly discovered edge is processed

                self.dfs(e.v)
        
        self.time += 1

        # all descendents have been processed
        self.exit_time[u] = self.time

        # after outedges are processed
        self.process_vertex_late(u)


    def process_edge(self, u, v):
        edge_class = self.edge_classification(u, v)

        print(u, v, edge_class)

        if edge_class is EdgeType.TREE:
            self.tree_out_degree[u] += 1

        # detect the highest reachable ancestor 
        if edge_class is EdgeType.BACK and self.parents[u] != v:
            if v in self.entry_time and self.entry_time[v] < self.entry_time[self.reachable_ancestor[u]]:
                self.reachable_ancestor[u] = v

                print(u, v, self.tree_out_degree[u])


if __name__ == "__main__":
    g = ArticulationGraph(GraphType.DIRECTED)

    # articulation graph

    # The Algorithm Design Manual
    # pg. 171 
    g.insert_edges([
        (1, 2, 0), (2, 3, 0), (3, 4, 0), (4, 5, 0),
        (5, 2, 0), (5, 1, 0), (1, 6, 0)
    ])

    g.dfs(1)