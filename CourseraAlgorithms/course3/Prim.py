
def load(filename):
    with open(filename) as f:
        line = f.readline()
        line = line.split()
        n_vertices, n_edges = int(line[0]), int(line[1])
        line = f.readline()
        with line:
            line = line.split()

