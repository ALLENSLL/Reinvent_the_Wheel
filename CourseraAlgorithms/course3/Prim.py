import heapq
from graph import *


def load(filename):
    with open(filename) as f:
        line = f.readline()
        line = line.split()
        n_vertices, n_edges = int(line[0]), int(line[1])
        graph = Graph(n_vertices)
        for i in range(n_edges):
            line = f.readline().split()
            edge = Edge(int(line[0]), int(line[1]), int(line[2]))
            graph.add(edge)
    return graph


def prim(graph, root=1):

    Queue = list()
    for i in range(graph.n_vertices):
        if i+1 != root:
            cost = graph.getCost(root, i+1)
            Queue.append(Vertice(i+1, root, cost))
    heapq.heapify(Queue)

    mst = list()
    mst.append(Vertice(root, None, 0))

    while len(Queue):
        u = heapq.heappop(Queue)
        mst.append(u)

        for edge in graph.graph[u.index-1]:
            index = edge.start if edge.end == u.index else edge.end

        #     for v in Queue:
        #         if (v.index == index) and (graph.getCost(u.index, v.index) < v.key):
        #             v.parents = u.index
        #             v.key = graph.getCost(u.index, v.index)
        # heapq.heapify(Queue)

            for i in range(len(Queue)):
                v = Queue[i]
                if (v.index == index) and (graph.getCost(u.index, v.index) < v.key):
                    v.parents = u.index
                    v.key = graph.getCost(u.index, v.index)

                    Queue[i] = Queue[-1]
                    Queue.pop()
                    if i < len(Queue):
                        heapq._siftup(Queue, i)
                        heapq._siftdown(Queue, 0, i)
                    heapq.heappush(Queue, v)


    return mst


if __name__ == '__main__':
    graph = load('edges.txt')
    mst = prim(graph)
    print(sum([v.key for v in mst]))