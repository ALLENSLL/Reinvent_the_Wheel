def kruskal(graph):
    assert type(graph)==dict

    nodes = graph.keys()   
    treeSet = []
    
    for node in nodes:
        temp = set()
        temp.add(node)
        treeSet.append(temp)
    path = []
    
    def find(left,right):
        for i in range(len(treeSet)):
            if left in treeSet[i]:
                if right in treeSet[i]:
                    return True
                else:
                    return False
    def update(left,right):
        for i in range(len(treeSet)):
            if left in treeSet[i]:
                for k in range(len(treeSet)):
                    if right in treeSet[k]:
                        treeSet[i] = treeSet[i] | treeSet[k]
                        treeSet.remove(treeSet[k])
                        return

    while len(treeSet) != 1:
        distance = float('inf') 
        for u in nodes:
            for v in nodes:
                if find(u,v) or u == v:
                    continue
                if graph[u][v] < distance:
                    distance = graph[u][v]
                    left = u
                    right = v
        path.append((left, right))
        update(left,right)
    return path


def prim(graph,root=False):
    assert type(graph) == dict
    
    nodes = list(graph.keys())
    if root == False:
        root = nodes[0]
        nodes.remove(root)
    else:
        nodes.remove(root)
    visited = [root]
    path = []
    
    while nodes:
        distance = float('inf')
        for u in visited:
            for v in graph[u]:
                if v in visited or u == v:
                    continue
                elif graph[u][v] < distance:
                    distance = graph[u][v]
                    left = u
                    right = v
        path.append((left,right))
        visited.append(right)
        nodes.remove(right)
    return path
        
if __name__ == '__main__':
    graph_dict = {'a': {'a':0,'b':4,'c':float('inf'),'d':float('inf'),'e':float('inf'),'f':float('inf'),'g':float('inf'),'h':8,'i':float('inf')},\
                    'b': {'a':4,'b':0,'c':8,'d':float('inf'),'e':float('inf'),'f':float('inf'),'g':float('inf'),'h':11,'i':float('inf')},\
                    'c': {'a':float('inf'),'b':8,'c':0,'d':7,'e':float('inf'),'f':4,'g':float('inf'),'h':float('inf'),'i':2},\
                    'd': {'a':float('inf'),'b':float('inf'),'c':7,'d':0,'e':9,'f':14,'g':float('inf'),'h':float('inf'),'i':float('inf')},\
                    'e': {'a':float('inf'),'b':float('inf'),'c':float('inf'),'d':9,'e':0,'f':10,'g':float('inf'),'h':float('inf'),'i':float('inf')},\
                    'f': {'a':float('inf'),'b':float('inf'),'c':4,'d':14,'e':10,'f':0,'g':2,'h':float('inf'),'i':float('inf')},\
                    'g': {'a':float('inf'),'b':float('inf'),'c':float('inf'),'d':float('inf'),'e':float('inf'),'f':2,'g':0,'h':1,'i':6},\
                    'h': {'a':8,'b':11,'c':float('inf'),'d':float('inf'),'e':float('inf'),'f':float('inf'),'g':1,'h':0,'i':7},\
                    'i': {'a':float('inf'),'b':float('inf'),'c':2,'d':float('inf'),'e':float('inf'),'f':float('inf'),'g':6,'h':7,'i':0},\
                    }

    print(kruskal(graph_dict))
    print(prim(graph_dict))