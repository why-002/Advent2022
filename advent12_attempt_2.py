class Hill:
    hill_set = set()

    def __init__(self, height, x, y):
        self.height = height
        self.x = int(x)
        self.y = int(y)
        self.final = True if self.height == -28 else False
        self.starting = True if self.height == -14 else False
        self.distance = 0 if self.height == -14 or self.height == 0 else float('inf')

        self.height = 0 if self.height == -14 else self.height
        self.height = 25 if self.height == -28 else self.height

        self.left = None
        self.right = None
        self.down = None
        self.up = None

        Hill.hill_set.add(self)

    def __lt__(self, other):
        if self.final is True or self.distance == float('inf'):
            return False
        return self.distance < other.distance

    def update_distance(self):
        dir_list = [self.up, self.down, self.left, self.right]
        dir_list = filter(lambda x: x is not None, dir_list)
        for direction in dir_list:
            direction.distance = self.distance + 1 if self.distance + 1 < direction.distance else direction.distance

    def __repr__(self):
        return str(self.height)

    def create_links(self):
        for i in Hill.hill_set:
            if self.height + 1 < i.height:
                pass
            else:
                if i.x == self.x + 1 and i.y == self.y:
                    self.right = i
                if i.x == self.x - 1 and i.y == self.y:
                    self.left = i
                if i.x == self.x and i.y == self.y + 1:
                    self.down = i
                if i.x == self.x and i.y == self.y - 1:
                    self.up = i

if __name__ == '__main__':
    with open('input12.txt', 'r') as fp:
        file = []
        for index, line in enumerate(fp):
            line = line.strip()
            line = [Hill(ord(value) - 97, i, index) for i, value in enumerate(line)]
            file += [line]

    h = Hill.hill_set.copy()

    for i in h:
        i.create_links()
    count = 0
    try:
        while True:
            active = min(h)
            active.update_distance()
            count += 1
            h.remove(active)

    except:
        for i in Hill.hill_set:
            if i.final is True:
                print(i.distance)

    Hill.hill_set = set()

    with open('input12.txt', 'r') as fp:
        file = []
        for index, line in enumerate(fp):
            line = line.strip()
            line = [Hill(ord(value) - 97, i, index) for i, value in enumerate(line)]
            file += [line]

    h = Hill.hill_set.copy()

    for i in h:
        i.create_links()
        if i.starting is True:
            i.distance = -1
    count = 0

    try:
        while True:
            active = min(h)
            if active.distance == -1:
                active.distance = 0
            active.update_distance()
            count += 1
            h.remove(active)

    except:
        for i in Hill.hill_set:
            if i.final is True:
                print(i.distance)