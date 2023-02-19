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


def attempt_two(starting, current_volcano):
    order = []
    pipes = [i.name for i in current_volcano.pipes if i.flow_rate != 0 and i.used is False]
    results = {}
    while pipes:
        pipe_test = itertools.permutations(pipes, 2)
        for p in pipe_test:
            test = find_final_pressure(starting, current_volcano, order + list(p))
            reverse_test = find_final_pressure(starting, current_volcano, order + list(p)[::-1])
            results[p] = test if test >= reverse_test else 0

        results = {i: j for i, j in results.items() if j != 0}
        interp = [i[0] for i, j in results.items() if j != 0]
        highest = None
        counts = 0
        for i in interp:
            if interp.count(i) >= counts:
                highest = i
                counts = interp.count(i)
        if len(pipes) == 1:
            highest = pipes[0]

        if highest is None:
            break
        order.append(highest)
        current_volcano.pipe_dict[highest].used = True
        pipes = [i.name for i in current_volcano.pipes if i.flow_rate != 0 and i.used is False]
        results = {}

    '''score = 0
    combinator = itertools.permutations(results, len(results))
    for comb in combinator:
        comb = [i for i in comb]
        current_score = find_final_pressure(starting, current_volcano, comb.copy())
        if current_score > score:
            print(comb)
            score = current_score
        print(score)'''
    score = find_final_pressure('AA', current_volcano, order)
    return score


def brute(starting, current_volcano):
    results = [i.name for i in current_volcano.pipes if i.flow_rate != 0]
    combinator = itertools.permutations(results, 6)
    score = 0
    for comb in combinator:
        comb = [i for i in comb]
        current_score = find_final_pressure(starting, current_volcano, tuple(comb.copy()))
        if current_score > score:
            score = current_score
    return score


def attempt_3(starting, current_volcano, use=None):
    if use is None:
        use = []
    try:
        distances = current_volcano.set_distances(use[-1])
    except IndexError:
        distances = current_volcano.set_distances(starting)
    vals = {}
    for pipe in [i for i in current_volcano.pipes if distances[i.name] != 0]:
            try:
                vals[pipe.name] = (find_final_pressure(starting, current_volcano, tuple(use +[use[-1]]+ [pipe.name])) - find_final_pressure(starting, current_volcano, tuple(use + [use[-1]]))) / distances[pipe.name] ** 2
            except IndexError:
                vals[pipe.name] = (find_final_pressure(starting, current_volcano, tuple(use + [pipe.name])) - find_final_pressure(starting, current_volcano, tuple(use))) / distances[pipe.name] ** 2
    vals = {i:j for i,j in vals.items() if i not in use}
    for index, value in vals.items():
        if value is max(vals.values()) and value != 0:
            return [index] + attempt_3(starting,current_volcano,use + [index])
    return []

def funny_idea(current_volcano, use=None):
    vals = {}
    for starting in [i.name for i in current_volcano.pipes if i.flow_rate != 0 or i.name == 'AA']:
        distances = {i:j for i,j in current_volcano.set_distances(starting).items() if current_volcano.pipe_dict[i].flow_rate != 0 and starting != i}
        distances = {i: j for i, j in distances.items() if j <= min(distances.values()) + 1}
        print(starting)
        print(distances)
        for i,j in distances.items():
            rate = current_volcano.pipe_dict[i].flow_rate
            rate /= 2 if j > min(distances.values()) else 1
            if rate == max(current_volcano.pipe_dict[i].flow_rate for i,j in distances.items()):
                print(i, current_volcano.pipe_dict[i].flow_rate)
        '''for target in [i.name for i in current_volcano.pipes if i.flow_rate != 0 and i.name != starting]:
            vals[target] = (find_final_pressure('AA', current_volcano, (starting,target)) - find_final_pressure('AA', current_volcano, tuple([starting]))) / distances[target]
            print(target, vals[target])'''
        print()

if __name__ == '__main__':
    pipes = interpret_file('test16.txt')
    v = Volcano(pipes)

    use = attempt_3('AA', v)
    print(use)
    score = find_final_pressure('AA', v, tuple(use))
    print(score)
    funny_idea(v)
    print(brute('AA', v))

# 2058, 2203 too low, 2396 too high not 2228 not 2257 not 1950

# TODO rewrite brute type algo so it loops for each layer individually that way you can cut off stuff that is too long and arbitrarily limit against going too far away
