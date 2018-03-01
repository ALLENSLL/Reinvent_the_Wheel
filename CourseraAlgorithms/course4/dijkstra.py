import heapq
from graph import *


class Dijkstra:
    def __init__(self, filename=None, n_vertices=None, n_edges=None, graph=None):
        if filename is not None:
            with open(filename) as f:
                line = f.readline().split()
                self._n_vertices = int(line[0])
                self._n_edges = int(line[1])
                inf = float('inf')
                self._graph = [[inf for i in range(self._n_vertices)] for j in range(self._n_vertices)]
                for i in range(self._n_vertices):
                    self._graph[i][i] = 0
                for i in range(self._n_edges):
                    tail, head, length = map(int, f.readline().split())
                    self._graph[tail-1][head-1] = length
        else:
            assert n_vertices == len(graph)
            self._n_vertices = n_vertices
            self._n_edges = n_edges
            self._graph = graph

    def run(self, src):
        src -= 1
        nodes = [i for i in range(self._n_vertices)]

        visited = [src]
        path = {}
        for node in nodes:
            path[node] = []
        nodes.remove(src)
        distance_graph = {src+1: 0}

        while nodes:
            distance = float('inf')
            for u in visited:
                for v in nodes:
                    new_dist = self._graph[src][u] + self._graph[u][v]
                    if new_dist <= distance:
                        distance = new_dist
                        next = v
                        pre = u
                        self._graph[src][v] = new_dist
            path[next] = [i for i in path[pre]]
            path[next].append(next)
            distance_graph[next+1] = distance
            visited.append(next)
            nodes.remove(next)
            dist = list()
        for i in range(self._n_vertices):
            dist.append(distance_graph[i+1])
        return dist, path

if __name__ == '__main__':
    dijkstra = Dijkstra(filename='g2.txt')
    dist, path = dijkstra.run(1)
    print(dist)
    dist, path = dijkstra.run(2)
    print(dist)

