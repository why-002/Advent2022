import itertools
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


def find_final_pressure(starting, current_volcano, use):
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
            reverse_test = find_final_pressure(starting,current_volcano, order + list(p)[::-1])
            results[p] = test if test >= reverse_test else 0

        results = {i:j for i,j in results.items() if j != 0}
        interp = [i[0] for i,j in results.items() if j!= 0]
        highest = None
        counts = 0
        for i in interp:
            if interp.count(i) >= counts:
                highest = i
                counts = interp.count(i)
                print(counts)
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
    print(order)
    score = find_final_pressure('AA', current_volcano, order)
    return score

def brute(starting, current_volcano):
    results = [i.name for i in current_volcano.pipes if i.flow_rate != 0]
    combinator = itertools.permutations(results, 6)
    score = 0
    for comb in combinator:
        comb = [i for i in comb]
        current_score = find_final_pressure(starting, current_volcano, comb.copy())
        if current_score > score:
            score = current_score
            print(score)
    return score

if __name__ == '__main__':
    pipes = interpret_file('input16.txt')
    v = Volcano(pipes)

    score = attempt_two('AA', v)
    print(score)

# 2058, 2203 too low, 2396 too high not 2228 not 2257 not 1950
