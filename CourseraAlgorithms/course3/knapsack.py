class Knapsack:

    def __init__(self, filename):
        self._size = 0
        self._n_items = 0
        self._values = list()
        self._weights = list()
        self._results = list()

        with open(filename) as f:
            line = f.readline().split()
            self._size, self._n_items = int(line[0]), int(line[1])
            for i in range(self._n_items):
                line = f.readline().split()
                self._values.append(int(line[0]))
                self._weights.append(int(line[1]))

        for i in range(self._n_items+1):
            self._results.append([])

    def dynamic_programming(self):
        for i in range(self._size+1):
            self._results[0].append(0)
        for i in range(1, self._n_items+1):
            for x in range(self._size+1):
                a = self._results[i-1][x]
                if x - self._weights[i-1] < 0:
                    b = 0
                else:
                    b = self._results[i-1][x-self._weights[i-1]] + self._values[i-1]
                self._results[i].append(max(a, b))
        return self._results[self._n_items][self._size]


if __name__ == '__main__':
    knapsack = Knapsack('knapsack.txt')
    print(knapsack.dynamic_programming())