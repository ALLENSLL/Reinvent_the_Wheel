from graph import *
import cProfile


class BellmanFord:
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

        inf = float('inf')
        self._distances = []
        for i in range(self._n_edges):
            self._distances.append([inf for j in range(self._n_vertices)])

    def run(self, source):
        self._distances[0][source-1] = 0
        for i in range(1, self._n_vertices):
            for v in range(1, self._n_vertices+1):
                a = self._distances[i-1][v-1]
                b = float('inf')
                for w in self._graph.getAdjPoints(v):
                    dis = self._distances[i-1][w-1] + self._graph.getLength(v, w)
                    if b > dis:
                        b = dis
                self._distances[i][v-1] = min(a, b)

    def hasNCC(self):
        return not self._distances[self._n_vertices-1] == self._distances[self._n_vertices-2]


if __name__ == '__main__':
    bellmanFord = BellmanFord('g1.txt')
    bellmanFord.run(1)
    print(bellmanFord.hasNCC())
    # cProfile.run('bellmanFord.run(1)')