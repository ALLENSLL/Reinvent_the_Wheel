import math


def convert(numbers):
    n = len(numbers)
    graph = []
    for i in range(n):
        graph.append([])
        m = len(numbers[i])
        for j in range(1, m):
            graph[i].append([int(numbers[i][0]), int(numbers[i][j])])
    return graph


def load(filename):
    f = open(filename, 'r')
    numbers = []
    line = f.readline()
    while line:
        line = line.split()
        numbers.append(line)
        line = f.readline()
    f.close()
    return convert(numbers)


def random_contraction(graph):
    graph_copy = graph
    while len(graph_copy) > 2:


    return cut_num, cut


def find_min_cut(graph, n_it):
    mincut_num = math.inf
    mincut = []
    for i in range(n_it):
        cut_num, cut = random_contraction(graph)
        if cut_num < mincut:
            mincut = cut
            mincut_num = cut_num
    return mincut_num, mincut


if __name__ == '__main__':
    a = load('test_random_contraction.txt')
    # n, cut = find_min_cut(a)
    print(a[0])