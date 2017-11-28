import math


def load(filename):
    f = open(filename, 'r')
    numbers = []
    line = f.readline()
    while line:
        line = line.split()
        numbers.append(line)
        line = f.readline()
    f.close()
    return numbers


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
    n, cut = find_min_cut(a)
    print(n)