def interpret_file(fname):
    with open(fname, 'r') as fp:
        blocks = []
        for line in fp:
            line = line.strip().split(',')
            line = (int(i) for i in line)
            line = tuple(line)
            blocks.append(line)
    return blocks


def find_sides(blocks, checks=None):
    if checks is None:
        checks = blocks
    total_sides = 0
    for block in blocks:
        sides = 6
        for check in checks:
            x_match = block[0] == check[0]
            y_match = block[1] == check[1]
            z_match = block[2] == check[2]
            matches = [x_match, y_match, z_match]
            if matches.count(True) == 2 and block != check:
                if x_match is False and abs(block[0] - check[0]) == 1:
                    sides -= 1
                elif y_match is False and abs(block[1] - check[1]) == 1:
                    sides -= 1
                elif z_match is False and abs(block[2] - check[2]) == 1:
                    sides -= 1
        total_sides += sides
    return total_sides


class Block:
    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]
        self.z = coords[2]
        self.distance = 0 if coords == (0, 0, 0) else float('inf')

    def __lt__(self, other):
        return self.distance < other.distance

    def __getitem__(self, item):
        if item == 0:
            return self.x
        if item == 1:
            return self.y
        if item == 2:
            return self.z
        raise IndexError


def remove_pocket_score(blocks):
    steps = set()
    x_vals = [i[0] for i in blocks]
    y_vals = [i[1] for i in blocks]
    z_vals = [i[2] for i in blocks]
    for x in range(max(x_vals) + 1):
        for y in range(max(y_vals) + 1):
            for z in range(max(z_vals) + 1):
                if (x, y, z) not in blocks:
                    steps.add(Block((x, y, z)))
    pockets = set()
    while steps:
        if min(steps).distance == float('inf'):
            pockets = [i for i in steps]
            steps = False
        else:
            active = min(steps)
            for i in steps:
                x_distance = abs(active.x - i.x)
                y_distance = abs(active.y - i.y)
                z_distance = abs(active.z - i.z)
                distances = [x_distance, y_distance, z_distance]
                if distances.count(0) == 2:
                    try:
                        distances.index(1)
                        i.distance = active.distance + 1 if active.distance + 1 < i.distance else i.distance
                    except ValueError:
                        pass
            steps.remove(active)
    checks = blocks + pockets
    current_score = find_sides(blocks, checks)
    return current_score


if __name__ == '__main__':
    blocks = interpret_file('input18.txt')
    current_score = find_sides(blocks)
    print(current_score)
    print(remove_pocket_score(blocks))

# 4040 too high, 2417 too low
