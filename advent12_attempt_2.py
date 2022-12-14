class Hill:
    hill_set = set()

    def __init__(self, height, x, y):
        self.height = height
        self.x = int(x)
        self.y = int(y)
        if self.height == -28:
            self.final = True
        else:
            self.final = False
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
        try:
            self.up.distance = self.distance + 1 if self.distance + 1 < self.up.distance or self.up.distance == float(
                'inf') else self.up.distance
        except AttributeError:
            pass
        try:
            self.down.distance = self.distance + 1 if self.distance + 1 < self.down.distance or self.down.distance == float(
                'inf') else self.down.distance
        except AttributeError:
            pass
        try:
            self.left.distance = self.distance + 1 if self.distance + 1 < self.left.distance or self.left.distance == float(
                'inf') else self.left.distance
        except AttributeError:
            pass
        try:
            self.right.distance = self.distance + 1 if self.distance + 1 < self.right.distance or self.right.distance == float(
                'inf') else self.right.distance
        except AttributeError:
            pass

    def __repr__(self):
        return str(self.height)

    def create_links(self):
        for i in Hill.hill_set:
            if i.x == self.x + 1 and i.y == self.y and self.height + 1 >= i.height:
                self.right = i
            if i.x == self.x - 1 and i.y == self.y and self.height + 1 >= i.height:
                self.left = i
            if i.x == self.x and i.y == self.y + 1 and self.height + 1 >= i.height:
                self.down = i
            if i.x == self.x and i.y == self.y - 1 and self.height + 1 >= i.height:
                self.up = i

if __name__ == '__main__':
    with open('input12.txt', 'r') as fp:
        file = []
        for index, line in enumerate(fp):
            line = line.strip()
            line = [Hill(ord(value) - 97, i, index) for i, value in enumerate(line)]
            file += [line]

print(file)

h = Hill.hill_set.copy()

for i in h:
    i.create_links()
count = 0
try:
    while True:
        active = min(h)
        active.update_distance()
        count += 1
        print(count)
        h.remove(active)

except:
    for i in Hill.hill_set:
        if i.final is True:
            print(i.distance)
