import itertools
from graph import *
from union_find import *

def load(filename):
    with open(filename) as f:
        line = f.readline()
        line = line.split()
        n_vertices = int(line[0])
        graph = Graph(n_vertices)
        line = f.readline()
        while line:
            line = line.split()
            edge = Edge(int(line[0]), int(line[1]), int(line[2]))
            graph.add(edge, duplicate=False)
            line = f.readline()
    return graph


def cluster(graph, k):

    assert k <= graph.n_vertices

    edges = list(itertools.chain.from_iterable(graph.graph))
    edges = sorted(edges)
    cls = range(1,graph.n_vertices+1)
    uf = UnionFind()
    uf.insert_objects(cls)
    i = j = 0
    while j < graph.n_vertices:
        if (graph.n_vertices - i) == k:
            while uf.find(edges[j].start) == uf.find(edges[j].end):
                j += 1
            return edges[j].cost
        edge = edges[j]
        j += 1
        if uf.find(edge.start) != uf.find(edge.end):
            uf.union(edge.start, edge.end)
            i += 1


if __name__ == "__main__":
    graph = load('cluster1.txt')
    space = cluster(graph,4)
    print(space)