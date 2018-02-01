import copy
import sys, threading
from collections import Counter
import numpy as np

sys.setrecursionlimit(800000)
threading.stack_size(67108864)


def reverse_graph(edges):
    n = len(edges)
    rev_edges = copy.deepcopy(edges)
    [rev_edges[i].reverse() for i in range(n)]
    return rev_edges


def convert(n_vertices, edges):
    graph = []
    [graph.append([]) for i in range(n_vertices)]
    for edge in edges:
        graph[edge[0]-1].append(edge[1])
    return graph


def load(filename):
    f = open(filename, 'r')
    edges = []
    line = f.readline()
    while line:
        line = line.split()
        edges.append([int(x) for x in line])
        line = f.readline()
    f.close()
    return edges


def dfs_t(graph, source, res, t):
    res[source-1] = -1
    for i in graph[source-1]:
        if res[i-1] == 0:
            dfs_t(graph, i, res, t)
    t[0] += 1
    res[source-1] = t[0]
    return


def dfs_l(graph, source, res, l):
    res[source-1] = l
    for i in graph[source-1]:
        if res[i-1] == 0:
            dfs_l(graph, i, res, l)
    return


def dfs_loop(graph, order, obtain):
    n_vertices = len(order)
    res = [0] * n_vertices

    if obtain == 'finishingtimes':
        t = [0]
        for i in order:
            if res[i-1] == 0:
                dfs_t(graph, i, res, t)
        res = list(np.argsort(res)+1)
    elif obtain == 'leaders':
        for i in range(n_vertices-1, -1, -1):
            source = order[i]
            if res[source-1] == 0:
                dfs_l(graph, source, res, i)

    return res


def kosaraju(n_vertices, edges):
    rev_graph = convert(n_vertices, reverse_graph(edges))
    order = list(range(1, n_vertices+1))
    order = dfs_loop(rev_graph, order, 'finishingtimes')
    graph = convert(n_vertices, edges)
    leaders = dfs_loop(graph, order, 'leaders')
    return leaders


def count(leaders):
    counts = Counter(leaders)
    res = [v for v in counts.values()]
    res.sort()
    return res[::-1]


def main():
    # a = load('test_SCC2.txt')
    # leaders = kosaraju(875714, a)
    a = load('test_SCC.txt')
    leaders = kosaraju(12, a)
    print(count(leaders))

if __name__ == '__main__':
    thread = threading.Thread(target=main)
    thread.start()
