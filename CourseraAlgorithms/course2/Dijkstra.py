

def load(filename, n_vetrices):
    f = open(filename, 'r')
    graph = [[1000001 for i in range(n_vetrices)] for i in range(n_vetrices)]
    line = f.readline()
    while line:
        line = line.split()
        i = int(line[0])
        graph[i-1][i-1] = 0
        for vetrix in line[1:]:
            j_w = vetrix.split(',')
            j, w = int(j_w[0]), int(j_w[1])
            graph[i-1][j-1] = w
        line = f.readline()
    f.close()
    return graph


def dijkstra(graph, src):
    length = len(graph)
    nodes = [i for i in range(length)]

    visited = [src]
    path = {}
    for node in nodes:
        path[node] = []
    nodes.remove(src)
    distance_graph = {src: 0}

    while nodes:
        # distance = float('inf')
        distance = 1000000
        for u in visited:
            for v in nodes:
                new_dist = graph[src][u] + graph[u][v]
                if new_dist <= distance:
                    distance = new_dist
                    next = v
                    pre = u
                    graph[src][v] = new_dist
        path[next] = [i for i in path[pre]]
        path[next].append(next)
        distance_graph[next] = distance
        visited.append(next)
        nodes.remove(next)
    return distance_graph, path


if __name__ == '__main__':
    graph = load('test_shortest_path.txt', 200)
    sources = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
    dis, path = dijkstra(graph, 0)
    for source in sources:
        print(dis.get(source, 1000000))
