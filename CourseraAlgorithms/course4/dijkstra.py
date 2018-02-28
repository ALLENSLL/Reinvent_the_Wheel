import heapq
from graph import *


class Dijkstra:
    def __init__(self, filename):
        with open(filename) as f:
            line = f.readline().split()
            self._n_vertices = int(line[0])
            self._n_edges = int(line[1])

            self._graph = Graph(self._n_vertices)
            for i in range(self._n_edges):
                line = f.readline().split()
                edge = Edge(int(line[0]), int(line[1]), int(line[2]))
                self._graph.add(edge)

if __name__ == '__main__':
    dijkstra = Dijkstra('g1.txt')


