class Tree:
    def __init__(self, height, x, y, forest):
        self.height = int(height)
        self.x = x
        self.y = y
        self.above = [int(i[x]) for i in forest[:y]] + [-1]
        self.below = [int(i[x]) for i in forest[y + 1:]] + [-1]
        self.left = [int(i) for i in forest[y][:x]] + [-1]
        self.right = [int(i) for i in forest[y][x+1:]] + [-1]

    def visible(self):
        return (self.height > int(max(self.above))) or (self.height > int(max(self.below))) or (self.height > int(max(self.left))) or (self.height > int(max(self.right)))

    def find_scenic_score(self):
        l_list = [self.above,self.below,self.left, self.right]
        for l in l_list:
            l.remove(-1)
            if l == []:
                l.append(-1)
        self.above.reverse()
        self.left.reverse()

        above_list, below_list, left_list, right_list = [], [], [], []
        name_list = [above_list,below_list,left_list,right_list]
        factors = []
        for name_index,name in enumerate(name_list):
            list_from = l_list[name_index]
            factors.append([value for index, value in enumerate(list_from) if value > max(list_from[:index] + [0])])

        total = 1
        for fac in factors:
            total *= len(fac)
        return total


with open('input8.txt', 'r') as fp:
    fp = [_.strip() for _ in fp.readlines()]
    forest = []
    for line_index, line in enumerate(fp):
        l = []
        for index, value in enumerate(line):
            l.append(Tree(int(value), int(index), int(line_index), fp))
        forest += l
count = 0
for i in forest:
    if i.visible():
        count += 1
print(count)

m = 0
for i in forest:
    i = i.find_scenic_score()
    if i > m:
        m = i
print(m)