class MWIS:

    def __init__(self, filename):
        self._n_vertices = 0
        self._weights = list()
        self._sets = list()
        self._max = list()
        with open(filename) as f:
            self._n_vertices = int(f.readline())
            for i in range(self._n_vertices):
                self._weights.append(int(f.readline()))
                self._sets.append([])

    def count(self):
        self._max.append(self._weights[0])
        self._sets[0].append(0)
        if self._weights[0] > self._weights[1]:
            self._max.append(self._weights[0])
            self._sets[1].append(0)
        else:
            self._max.append(self._weights[1])
            self._sets[1].append(1)
        for i in range(2, self._n_vertices):
            m1 = self._max[i-1]
            m2 = self._max[i-2] + self._weights[i]
            if m1 > m2:
                self._max.append(m1)
                self._sets[i] = self._sets[i-1]
            else:
                self._max.append(m2)
                self._sets[i].extend(self._sets[i-2])
                self._sets[i].append(i)

    def get_answer(self):
        index = [1, 2, 3, 4, 17, 117, 517, 997]
        for i in index:
            if i-1 in self._sets[self._n_vertices-1]:
                print('1', end='')
            else:
                print('0', end='')


if __name__ == '__main__':

    mwis = MWIS('mwis.txt')
    mwis.count()
    mwis.get_answer()