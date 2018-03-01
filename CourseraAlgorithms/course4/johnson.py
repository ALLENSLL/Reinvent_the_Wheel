from bellman_ford import BellmanFord
from dijkstra import Dijkstra


class Johnson:
    def __init__(self, filename):
        with open(filename) as f:
            line = f.readline().split()
            self._n_vertices = int(line[0])
            self._n_edges = int(line[1])
            self._graph = [[float('inf') for i in range(self._n_vertices)] for j in range(self._n_vertices)]
            for i in range(self._n_vertices):
                self._graph[i][i] = 0
            for i in range(self._n_edges):
                tail, head, length = map(int, f.readline().split())
                self._graph[tail-1][head-1] = length
        self._weight = None
        self._distances = list()

    def reweight(self):
        graph = list()
        graph.append([0 for i in range(self._n_vertices+1)])
        for i in range(self._n_vertices):
            temp = [float('inf')]
            temp.extend(self._graph[i])
            graph.append(temp)
        bellmanFord = BellmanFord(n_vertices=self._n_vertices+1, n_edges=self._n_edges+self._n_vertices, graph=graph)
        self._weight = bellmanFord.run(1)
        if self._weight is None:
            return
        for i in range(self._n_vertices):
            for j in range(self._n_vertices):
                self._graph[i][j] = self._graph[i][j] + self._weight[i+1] - self._weight[j+1]

    def run(self):
        self.reweight()
        for i in range(self._n_vertices):
            dijkstra = Dijkstra(n_vertices=self._n_vertices, n_edges=self._n_edges, graph=self._graph)
            dist, path = dijkstra.run(i+1)
            for j in range(self._n_vertices):
                dist[j] = dist[j] - self._weight[i+1] + self._weight[j+1]
            self._distances.append(dist)
        return min(min(self._distances, key=lambda x: min(x)))

if __name__ == '__main__':
    johnson = Johnson('g1.txt')
    print(johnson.run())