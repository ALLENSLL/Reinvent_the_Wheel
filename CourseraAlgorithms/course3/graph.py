class Graph:
    def __init__(self, n_vertices):
        self.n_vertices = n_vertices
        self.n_edges = 0
        self.graph = list()

        for i in range(n_vertices):
            self.graph.append([])

    def add(self, edge, duplicate=True):
        if duplicate:
            self.graph[edge.start-1].append(edge)
        self.graph[edge.end-1].append(edge)
        self.n_edges += 1

    def getCost(self, start, end):
        for edge in self.graph[start-1]:
            if edge.start == end or edge.end == end:
                return edge.cost
        return float('inf')


class Edge:
    def __init__(self, start, end, cost):
        self.start = start
        self.end = end
        self.cost = cost

    def __eq__(self, other):
        return self.cost == other.cost #and self.start == other.start and self.end == other.end

    def __gt__(self, other):
        # if self.cost > other.cost:
        #     return True
        # elif self.start > other.start:
        #     return True
        # elif self.end > other.end:
        #     return True
        # else:
        #     return False
        return self.cost > other.cost

    def __lt__(self, other):
        # if self.cost < other.cost:
        #     return True
        # elif self.start < other.start:
        #     return True
        # elif self.end < other.end:
        #     return True
        # else:
        #     return False
        return self.cost < other.cost


class Vertice:
    def __init__(self, index=None, parents=None, key=float('inf')):
        self.index = index
        self.parents = parents
        self.key = key

    def __eq__(self, other):
        return self.key == other.key

    def __gt__(self, other):
        return self.key > other.key

    def __lt__(self, other):
        return self.key < other.key