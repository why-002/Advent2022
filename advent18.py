def interpret_file(fname):
    with open(fname, 'r') as fp:
        blocks = []
        for line in fp:
            line = line.strip().split(',')
            line = (int(i) for i in line)
            line = tuple(line)
            blocks.append(line)
    return blocks

def find_sides(blocks):
    total_sides = 0
    for line in blocks:
        sides = 6
        for b in blocks:
            x_match = b[0] == line[0]
            y_match = b[1] == line[1]
            z_match = b[2] == line[2]
            matches = [x_match, y_match, z_match]
            if matches.count(True) == 2 and b != line:
                if x_match is False and abs(b[0] - line[0]) == 1:
                    sides -= 1
                elif y_match is False and abs(b[1] - line[1]) == 1:
                    sides -= 1
                elif z_match is False and abs(b[2] - line[2]) == 1:
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


def remove_pocket_score(blocks):
    steps = set()
    x_vals = [i[0] for i in blocks]
    y_vals = [i[1] for i in blocks]
    z_vals = [i[2] for i in blocks]
    for x in range(max(x_vals)+1):
        for y in range(max(y_vals)+1):
            for z in range(max(z_vals)+1):
                if (x,y,z) not in blocks:
                    steps.add(Block((x,y,z)))
    pockets = set()
    while steps:
        if min(steps).distance == float('inf'):
            pockets = steps.copy()
            break
        active = min(steps)
        for i in steps:
            x_distance = abs(active.x-i.x)
            y_distance = abs(active.y-i.y)
            z_distance = abs(active.z-i.z)
            distances = [x_distance, y_distance, z_distance]
            if distances.count(0) == 2:
                try:
                    distances.index(1)
                    i.distance = active.distance + 1
                except ValueError:
                    pass
        steps.remove(active)
    checks = blocks + [(i.x, i.y, i.z) for i in pockets]
    current_score = 0
    for b in blocks:
        sides = 6
        for c in checks:
            x_match = c[0] == b[0]
            y_match = c[1] == b[1]
            z_match = c[2] == b[2]
            matches = [x_match, y_match, z_match]
            if matches.count(True) == 2:
                if x_match is False and abs(c[0] - b[0]) == 1:
                    current_score -= 1
                elif y_match is False and abs(c[1] - b[1]) == 1:
                    current_score -= 1
                elif z_match is False and abs(c[2] - b[2]) == 1:
                    current_score -= 1
        current_score += sides
    return current_score


if __name__ == '__main__':
    blocks = interpret_file('input18.txt')
    current_score = find_sides(blocks)
    print(current_score)
    print(remove_pocket_score(blocks))

# 4040 too high, 2417 too low
