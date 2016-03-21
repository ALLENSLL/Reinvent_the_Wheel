# -*- coding:utf-8 -*-

def dijkstra(graph,src):
    length = len(graph)
    if type(graph) == list:
        nodes = [i for i in range(length)]
    elif type(graph) == dict:
        nodes = list(graph.keys())

    visited = [src]
    path = {}
    for node in nodes:
        path[node] = []
    nodes.remove(src)
    distance_graph = {src:0}
    
    while nodes:
        distance = float('inf')
        for u in visited:
            for v in nodes:
                new_dist = graph[src][u]+graph[u][v]
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
    return distance_graph,path
 
def floyd(graph):
    length = len(graph)
    path = {}
    
    for i in range(length):
        path[i] = {}
        for j in range(length):
            if i == j:
                continue
            path[i][j] = [i,j]
            new_node = None
            for k in range(length):
                if k == j:
                    continue
                new_len = graph[j][k] + graph[k][j]
                if graph[i][j] > new_len:
                    graph[i][j] = new_len
                    new_node = k
            if new_node:
                path[i][j].insert(-1,new_node)
    return graph, path
    
if __name__ == '__main__':
    graph = {'s':{'s':0,'t':10,'x':float('inf'),'z':float('inf'),'y':5},
             't':{'s':float('inf'),'t':0,'x':1,'z':float('inf'),'y':2},
             'x':{'s':float('inf'),'t':float('inf'),'x':0,'z':4,'y':float('inf')},
             'z':{'s':7,'t':float('inf'),'x':6,'z':0,'y':float('inf')},
             'y':{'s':float('inf'),'t':3,'x':9,'z':2,'y':0},
    }
    graph_list = [   [0, 2, 1, 4, 5, 1],
            [1, 0, 4, 2, 3, 4],
            [2, 1, 0, 1, 2, 4],
            [3, 5, 2, 0, 3, 3],
            [2, 4, 3, 4, 0, 1],
            [3, 4, 7, 3, 1, 0],]
    dis,path = dijkstra(graph_list,0)
    print(dis)
    print(path)
    dis,path = floyd(graph_list)
    print(dis)
    print(path)