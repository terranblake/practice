from structures.graph import Graph, GraphType, VertexState, EdgeType
from enum import Enum


class ArticulationGraph(Graph):

    def process_edge_creation(self, u, v):
        self.tree_out_degree[u] = 0


    def process_vertex_early(self, u):
        self.reachable_ancestor[u] = u


    # def edge_classification(self, u, v):
    #     if self.parents[v] == u:
    #         return EdgeType.TREE
    #     elif self.states[v] is VertexState.DISCOVERED:
    #         return EdgeType.BACK
    #     elif self.states[v] is VertexState.DISCOVERED and self.entry_time[v] > self.entry_time[u]:
    #         return EdgeType.FORWARD
    #     elif self.states[v] is VertexState.DISCOVERED and self.entry_time[v] < self.entry_time[u]:
    #         return EdgeType.CROSS

        # print('unclassified edge', u, v)


    def process_edge(self, u, v):
        edge_class = self.edge_classification(u, v)

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
    g.insert_edges([
        (1, 2, 0), (1, 8, 0), (2, 3, 0), (3, 5, 0),
        (3, 4, 0), (5, 6, 0), (6, 7, 0), (7, 3, 0),
        (8, 9, 0), (9, 0, 0), (0, 8, 0), (5, 2, 0), (5, 1, 0)
    ])

    g.dfs(1)