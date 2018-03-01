import cProfile


class BellmanFord:
    def __init__(self, filename=None, n_vertices=None, n_edges=None, graph=None):
        if filename is not None:
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
        else:
            assert n_vertices == len(graph)
            self._n_vertices = n_vertices
            self._n_edges = n_edges
            self._graph = graph
        self._distances = None
        self._adjs = self.get_adj_points()

    def get_adj_points(self):
        adjs = list()
        for v in range(self._n_vertices):
            points = list()
            for i in range(self._n_vertices):
                if self._graph[i][v] != float('inf') and v != i:
                    points.append(i+1)
            # points.remove(v+1)
            adjs.append(points)
        return adjs

    def run(self, source):
        self._distances = [[float('inf') for i in range(self._n_vertices)] for j in range(self._n_edges)]
        self._distances[0][source-1] = 0
        for i in range(1, self._n_edges):
            for v in range(1, self._n_vertices+1):
                a = self._distances[i-1][v-1]
                b = float('inf')
                for w in self._adjs[v-1]:
                    dis = self._distances[i-1][w-1] + self._graph[w-1][v-1]
                    if b > dis:
                        b = dis
                self._distances[i][v-1] = min(a, b)
            if self._distances[i] == self._distances[i-1]:
                return self._distances[i]
        print('Graph has negative circle')
        return None


if __name__ == '__main__':
    bellmanFord = BellmanFord(filename='g1.txt')
    print(bellmanFord.run(1))
    # cProfile.run('bellmanFord.run(1)')