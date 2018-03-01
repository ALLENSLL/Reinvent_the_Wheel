import cProfile

class FloyedWarshall:
    def __init__(self, filename):
        with open(filename) as f:
            line = f.readline().split()
            self._n_vertices = int(line[0])
            self._n_edges = int(line[1])
            self._edges = {}
            for i in range(self._n_edges):
                tail, head, length = map(int, f.readline().split())
                self._edges[(tail, head)] = length
        inf = float('inf')
        self._distances = [[inf for j in range(self._n_vertices)] for i in range(self._n_vertices)]

    def run(self):
        for i in range(self._n_vertices):
            for j in range(self._n_vertices):
                if i == j:
                    self._distances[i][j] = 0
                elif (i+1, j+1) in self._edges:
                    self._distances[i][j] = self._edges[(i+1, j+1)]
        for k in range(self._n_vertices):
            for i in range(self._n_vertices):
                for j in range(self._n_vertices):
                    dis = self._distances[i][k] + self._distances[k][j]
                    if dis < self._distances[i][j]:
                        self._distances[i][j] = dis

                    if i == j and self._distances[i][j] < 0:
                        return "Graph has negative cycle"
        return min(min(self._distances, key=lambda x: min(x)))


if __name__ == '__main__':
    # cProfile.run('floyedWarshall = FloyedWarshall("g1.txt")')
    floyedWarshall = FloyedWarshall('g1.txt')
    print(floyedWarshall.run())