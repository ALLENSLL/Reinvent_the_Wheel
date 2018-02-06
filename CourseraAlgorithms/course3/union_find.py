class UnionFind:

    def __init__(self):
        self.num_ranks = {}
        self.leaders = {}
        self.num_to_objects = {}
        self.objects_to_num = {}
        self.__repr__ = self.__str__

    def insert_objects(self, objects):
        for obj in objects:
            self.find(obj)

    def find(self, obj):
        if obj not in self.objects_to_num:
            n_obj = len(self.objects_to_num)
            self.num_ranks[n_obj] = 0
            self.objects_to_num[obj] = n_obj
            self.num_to_objects[n_obj] = obj
            self.leaders[n_obj] = n_obj
            return obj
        need_update_leader = [self.objects_to_num[obj]]
        par = self.leaders[need_update_leader[-1]]
        while par != need_update_leader[-1]:
            need_update_leader.append(par)
            par = self.leaders[par]
        for i in need_update_leader:
            self.leaders[i] = par
        return self.num_to_objects[par]

    def union(self, object1, object2):
        leader1 = self.find(object1)
        leader2 = self.find(object2)
        if leader1 != leader2:
            num1 = self.objects_to_num[leader1]
            num2 = self.objects_to_num[leader2]
            w1 = self.num_ranks[num1]
            w2 = self.num_ranks[num2]
            if w1 == w2:
                self.leaders[num2] = num1
                self.num_ranks[num2] += 1
            elif w1 < w2:
                self.leaders[num1] = num2
            else:
                self.leaders[num2] = num1

    def count(self):
        return len(set(self.leaders.values()))

    def __str__(self):
        sets = {}
        for i in range(len(self.objects_to_num)):
            sets[i] = []
        for i in self.objects_to_num:
            sets[self.objects_to_num[self.find(i)]].append(i)
        out = []
        for i in sets.values():
            if i:
                out.append(repr(i))
        return ','.join(out)