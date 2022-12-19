class Sand:
    sand_list = []

    def __init__(self, prev=None):
        self.position = (500, 0)
        self.x_position = self.position[0]
        self.y_position = self.position[1]
        Sand.sand_list.append(self)
        self.previous_position = (500, 0)
        self.previous_sand = prev

        if self.previous_sand is not None:
            self.position = self.previous_sand.previous_position
            self.x_position = self.position[0]
            self.y_position = self.position[1]

    def test(self, x_incr: int, y_incr: int) -> tuple[int, int]:
        return self.position[0] + x_incr, self.position[1] + y_incr

    def update_position(self, increment_position: list):
        self.previous_position = self.position
        self.x_position += increment_position[0]
        self.y_position += increment_position[1]
        self.position = (self.x_position, self.y_position)

    def check_if_over_abyss(self, occupied: set):
        occupied = [i for i in occupied if i[0] == self.x_position and i[1] > self.y_position]
        if not occupied:
            return True
        else:
            return False


class Cave:
    def __init__(self, rocks):
        self.occupied: set = rocks

    def __call__(self):
        self.active = Sand()

        while True:
            if self.active.test(0, 1) not in self.occupied:
                self.active.update_position([0, 1])
                result = self.active.check_if_over_abyss(self.occupied)
                if result:
                    return len(Sand.sand_list)-1

            elif self.active.test(-1, 1) not in self.occupied:
                self.active.update_position([-1, 1])

            elif self.active.test(1, 1) not in self.occupied:
                self.active.update_position([1, 1])

            else:
                if self.active.position == (500, 0):
                    return len(Sand.sand_list)
                self.occupied.add(self.active.position)
                self.active = Sand(self.active)

    def cave2(self):
        self.active = Sand()
        y_vals = [i[1] for i in self.occupied]
        floor = max(y_vals) + 1

        while True:
            if self.active.y_position == floor:
                self.occupied.add(self.active.position)
                self.active = Sand(self.active)

            if self.active.test(0, 1) not in self.occupied:
                self.active.update_position([0, 1])

            elif self.active.test(-1, 1) not in self.occupied:
                self.active.update_position([-1, 1])

            elif self.active.test(1, 1) not in self.occupied:
                self.active.update_position([1, 1])

            else:
                if self.active.position == (500, 0):
                    return len(Sand.sand_list)
                self.occupied.add(self.active.position)
                self.active = Sand(self.active)

def interpret_cave(filename: str) -> set:
    with open(filename, 'r') as fp:
        occupied = set()
        for line in fp:
            line = line.split()

            while '->' in line:
                line.remove('->')

            try:
                for index,point in enumerate(line):

                    current_x, current_y = point.split(',')
                    next_x, next_y = line[index + 1].split(',')

                    current_x, current_y, next_x, next_y = int(current_x), int(current_y), int(next_x), int(next_y)

                    if current_x == next_x:
                        lower = min([current_y, next_y])
                        upper = max([current_y, next_y]) + 1
                        for i in range(lower, upper):
                            occupied.add((current_x, i))

                    elif current_y == next_y:
                        lower = min((current_x, next_x))
                        upper = max((current_x, next_x)) + 1
                        for i in range(lower, upper):
                            occupied.add((i, current_y))

            except IndexError:
                pass
        return occupied


if __name__ == '__main__':
    occupied = interpret_cave('input14.txt')
    c = Cave(occupied)
    print(c())

    occupied2 = interpret_cave('input14.txt')
    Sand.sand_list = []
    l = Cave(occupied2)
    print((l.cave2()))
#part 26100 > 2 > 1826