import itertools
from functools import cache


class Volcano:
    totals = []

    def __init__(self, pipes):
        self.pipes: list[Pipe] = pipes
        self.pipe_dict = {i.name: i for i in self.pipes}
        for i in self.pipes:
            i.set_connections()

    def set_distances(self, starting: str):

        for i in self.pipes:
            i.distance = float('inf')
            if i.name == starting:
                i.distance = 0

        pipes = set(self.pipes)
        while pipes:
            active = min(pipes)
            pipes.remove(active)
            for i in pipes:
                if i in active.connections and active.distance + 1 < i.distance:
                    i.distance = active.distance + 1
        return {i.name: i.distance for i in self.pipes}


class Pipe:
    pipe_list = []

    def __init__(self, name, flow_rate, connections):
        self.name = name
        self.flow_rate = flow_rate
        self.connection_names = connections
        self.used = False
        self.connections = []
        Pipe.pipe_list.append(self)
        self.distance = float('inf')
        self.ordering = None

    def __lt__(self, other):
        return self.distance < other.distance

    def __repr__(self):
        return self.name

    def set_connections(self):
        for i in Pipe.pipe_list:
            if i.name in self.connection_names:
                self.connections.append(i)


def interpret_file(fname):
    pipes = []
    with open(fname, 'r') as fp:
        for line in fp:
            line = line.strip().split()
            name = line[1]
            flow = int(line[4][:-1].strip('rate='))

            try:
                ind = line.index('valves')
            except ValueError:
                ind = line.index('valve')

            leads_to = line[ind + 1:]
            for index, string in enumerate(leads_to):
                leads_to[index] = string.strip(',')

            pipes.append(Pipe(name, flow, leads_to))

    return pipes


def find_scores(prev, v, used):
    v.set_distances(prev)
    eq_dict = {}
    for i in v.pipes:
        if i.distance != 0 and i.flow_rate != 0 and i.name not in used:
            eq_dict[i.name] = i.flow_rate / (i.distance ** 2)
    max_num = max(eq_dict.values())
    for i, j in eq_dict.items():
        if j == max_num:
            return i


def find_path(starting, v):
    current = find_scores('AA', v, [])

    use = []
    use += [current]
    while len(use) < len([i for i in v.pipes if i.flow_rate > 0]):
        current = find_scores(current, v, use)
        use += [current]
    return use

@cache
def find_final_pressure(starting, current_volcano, use):
    use = list(use)
    count = 0
    current = starting
    rate = 0
    pressure = 0
    while count < 30:
        distances = current_volcano.set_distances(current)
        try:
            current = use.pop(0)
            for _ in range(distances[current] + 1):
                if count < 30:
                    pressure += rate
                    count += 1
            rate += current_volcano.pipe_dict[current].flow_rate
        except IndexError:
            pressure += rate
            count += 1
    return pressure


def graphical_attempt(starting:str, v:Volcano):
    distances = v.set_distances('AA')
    pipeset = set()
    pipeorder = []
    for pipe in Pipe.pipe_list:
        try:
            pipe.ordering = pipe.flow_rate / pipe.distance
        except ZeroDivisionError:
            pipe.ordering = 0
        pipeset.add((pipe.name,pipe.ordering))
    while pipeset:
        remove = ('NaN', -1)
        for i in pipeset:
            remove = i if i[1] > remove[1] else remove
        pipeorder.append(remove)
        try:
            pipeset.remove(remove)
        except:
            pass
    return [i[0] for i in pipeorder]



if __name__ == '__main__':
    pipes = interpret_file('input16.txt')
    v = Volcano(pipes)

    use = graphical_attempt('AA', v)
    print(use)
    score = find_final_pressure('AA', v, tuple(use))
    print(score)

# 2058, 2203 too low, 2396 too high not 2228 not 2257 not 1950

# TODO rewrite brute type algo so it loops for each layer individually that way you can cut off stuff that is too long and arbitrarily limit against going too far away
