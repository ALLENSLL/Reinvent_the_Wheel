import heapq
from graph import Vertice


class Huffman:

    def __init__(self, filename):
        self._nodes = list()
        self._queue = list()
        self._size = 0
        with open(filename) as f:
            self._n_symbols = int(f.readline())
            for i in range(self._n_symbols):
                weight = int(f.readline())
                new_vertice = Vertice(i, None, weight)
                self._nodes.append(new_vertice)
                self._queue.append(new_vertice)
                self._size += 1

    def code(self):
        heapq.heapify(self._queue)

        while len(self._queue) != 1:
            min_1 = heapq.heappop(self._queue)
            min_2 = heapq.heappop(self._queue)
            new_vertice = Vertice(self._size, None, min_1.key+min_2.key)
            self._nodes[min_1.index].parents = new_vertice.index
            self._nodes[min_2.index].parents = new_vertice.index
            self._nodes.append(new_vertice)
            heapq.heappush(self._queue, new_vertice)
            self._size += 1

    def count(self):
        min_deep = float('inf')
        max_deep = 0
        for i in range(self._n_symbols):
            deep = 0
            vertice = self._nodes[i]
            while vertice.parents is not None:
                vertice = self._nodes[vertice.parents]
                deep += 1
            if deep > max_deep:
                max_deep = deep
            elif deep < min_deep:
                min_deep = deep
        return min_deep, max_deep


if __name__ == '__main__':
    huffman = Huffman("huffman.txt")
    huffman.code()
    print(huffman.count())
