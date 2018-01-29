
class Job:
    def __init__(self, weight, length):
        self.weight = weight
        self.length = length
        # self.index = weight - length
        self.index = weight / length

    def __eq__(self, other):
        return self.index == other.index

    def __gt__(self, other):
        return self.index > other.index

    def __lt__(self, other):
        return self.index < other.index


def load(filename):
    jobs = []
    with open(filename, 'r') as f:
        n_jobs = int(f.readline())
        line = f.readline()
        while line:
            line = line.split()
            jobs.append(Job(int(line[0]), int(line[1])))
            line = f.readline()

    return jobs


def greedy_difference(jobs):
    jobs.sort()
    jobs.reverse()
    sum = 0
    time = 0
    for job in jobs:
        time += job.length
        sum += time * job.weight

    return sum

if __name__ == '__main__':
    jobs = load('test_schedule_jobs.txt')
    print(greedy_difference(jobs))