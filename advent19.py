class BluePrint:
    blueprint_list = []
    def __init__(self, name, costs):
        self.name = name
        self.costs: dict[str:list] = costs
        BluePrint.blueprint_list.append(self)

def interpret_file(fname):
    with open(fname, 'r') as fp:
        for line in fp:
            name, line = line.strip().split(':')
            print(line)
            line = line.split('.')
            print(line)
            costs = {}
            for i in line:
                if i:
                    i = i.split(' ')
                    print(i)
                    costs[i[2]] = [int(num[0]) for num in i if num.isnumeric()]
            BluePrint(name, costs)
            print(costs)


if __name__ == '__main__':
    interpret_file('test19.txt')