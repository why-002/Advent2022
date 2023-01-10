class Monkey:
    monkey_dict = {}

    def __init__(self, name: str, instructions: list):
        self.name = name
        if len(instructions) == 1:
            self.number = int(instructions[0])
        else:
            self.number = False
            self.first, self.function, self.second = instructions
        Monkey.monkey_dict[self.name] = self

    def update_values(self):
        funcs = {
            '*': lambda x, y: int(x * y),
            '/': lambda x, y: int(x / y),
            '-': lambda x, y: int(x - y),
            '+': lambda x, y: int(x + y)
        }
        # TODO fix to be isinstance
        if type(self.number) == int:
            return True
        if type(Monkey.monkey_dict[self.first].number) == int and type(Monkey.monkey_dict[self.second].number) == int:
            print(self.first, self.second)
            self.number = funcs[self.function](Monkey.monkey_dict[self.first].number, Monkey.monkey_dict[self.second].number)
            return True
        return False
    def __repr__(self):
        return self.name


def interpret_file(fname):
    with open(fname, 'r') as fp:
        for line in fp:
            line = line.strip().split()
            name, func = line[0][:-1], line[1:]
            print(name, func)
            Monkey(name, func)

def simul(dictionary: dict):
    monkey_list = [i for i in dictionary.values()]
    while monkey_list:
        for monkey in monkey_list:
            check = monkey.update_values()
            if check:
                monkey_list.remove(monkey)
        print(monkey_list)
    return Monkey.monkey_dict['root'].number

if __name__ == '__main__':
    interpret_file('input21.txt')
    total = simul(Monkey.monkey_dict)
    print(total)
