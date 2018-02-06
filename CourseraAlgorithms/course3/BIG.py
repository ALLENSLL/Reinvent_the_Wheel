import itertools
from union_find import UnionFind

# test cases https://github.com/beaunus/stanford-algs/tree/master/testCases/course3/assignment2Clustering/question2


class BigCluster:

    def __init__(self, filename):
        with open(filename) as f:
            n_vertices, n_bits = f.readline().split()
            self._n_vertices = int(n_vertices)
            self._n_bits = int(n_bits)
            self._vertices = {}
            for index in range(1, self._n_vertices+1):
                line = f.readline().replace('\n', '').replace(' ', '')
                bits = ''.join(line)
                num = int(bits, 2)
                self._vertices[num] = (index, bits)

    def clustering(self):
        possible_dis = [2**i for i in range(self._n_bits)]
        possible_dis.extend([-dis for dis in possible_dis])
        for par in itertools.combinations(possible_dis, 2):
            possible_dis.append(sum(par))

        possible_dis.remove(0)
        uf = UnionFind()
        need_union = []
        for i in self._vertices.keys():
            for dis in possible_dis:
                if i+dis in self._vertices:
                    v_idnex, v_bits = self._vertices[i]
                    u_index, u_bits = self._vertices[i+dis]
                    if self._hamming(v_bits, u_bits) < 3:
                        need_union.append((v_idnex, u_index))

        for v, u in need_union:
            if uf.find(v) != uf.find(u):
                uf.union(v, u)

        return uf.count

    def _hamming(self, v, u):
        dis = 0
        for i in range(self._n_bits):
            if v[i] != u[i]:
                dis += 1
        return dis


if __name__ == "__main__":
    import  cProfile
    cProfile.run('big = BigCluster("clustering_big.txt")')
    # big = BigCluster("clustering_big.txt")
    cProfile.run('print(big.clustering())')
