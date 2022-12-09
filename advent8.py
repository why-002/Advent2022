class Tree:
    def __init__(self, height, x, y, forest):
        self.height = int(height)
        self.x = x
        self.y = y
        self.above = [int(i[x]) for i in forest[:y]]
        self.below = [int(i[x]) for i in forest[y + 1:]]
        self.left = [int(i) for i in forest[y][:x]]
        self.right = [int(i) for i in forest[y][x + 1:]]
        self.l_list = [self.above, self.below, self.left, self.right]
        self.score = 0
        self.factors = []
        self.above.reverse()
        self.left.reverse()

    def __repr__(self):
        return str(self.height)
    def __lt__(self, other):
        return self.score < other.score

    def visible(self):
        try:
            return (self.height > int(max(self.above))) or (self.height > int(max(self.below))) or (
                        self.height > int(max(self.left))) or (self.height > int(max(self.right)))
        except ValueError:
            return True

    def calculate_scenic_score(self):

        for index, list_from in enumerate(self.l_list):
            self.factors.append([value for index, value in enumerate(list_from) if max(list_from[:index] + [-1]) < self.height])

        total = 1
        for fac in self.factors:
            total *= len(fac)
        self.score = total


with open('input8.txt', 'r') as fp:
    fp = [_.strip() for _ in fp.readlines()]
    forest = []
    for line_index, line in enumerate(fp):
        l = []
        for index, value in enumerate(line):
            l.append(Tree(int(value), int(index), int(line_index), fp))
        forest.append(l)
    count = 0
    for line in forest:
        for i in line:
            if i.visible():
                count += 1
    print(count)
    print(forest)
    m = Tree(0, 0, 0, [[]])
    for line in forest:
        for i in line:
            if [] not in i.l_list:
                i.calculate_scenic_score()
                if m < i:
                    m = i
    print(m.score)
    print(m)
    print(*m.l_list, sep='\n')
    print(m.factors)
