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
        self.original_num = self.number

    def update_values(self):
        funcs = {
            '*': lambda x, y: int(x * y),
            '/': lambda x, y: int(x / y),
            '-': lambda x, y: int(x - y),
            '+': lambda x, y: int(x + y),
            '=': lambda x, y: x == y
        }
        # TODO fix to be isinstance
        if type(self.number) == int:
            return True
        if type(Monkey.monkey_dict[self.first].number) == int and type(Monkey.monkey_dict[self.second].number) == int:
            self.number = funcs[self.function](Monkey.monkey_dict[self.first].number,
                                               Monkey.monkey_dict[self.second].number)
            return True
        return False
    def normalize(self):
        self.number = self.original_num

    def __repr__(self):
        return self.name


def interpret_file(fname):
    with open(fname, 'r') as fp:
        for line in fp:
            line = line.strip().split()
            name, func = line[0][:-1], line[1:]
            Monkey(name, func)


def simul(dictionary: dict):
    monkey_list = [i for i in dictionary.values()]
    while monkey_list:
        for monkey in monkey_list:
            check = monkey.update_values()
            if check:
                monkey_list.remove(monkey)
    return dictionary['root'].number


def find_equals(dictionary: dict):
    for i in dictionary.values():
        i.normalize()
    dictionary['humn'].number = -1
    set_equal = [dictionary[dictionary['root'].first], dictionary[dictionary['root'].second]]

    def inner(monkey: Monkey):
        if monkey.number:
            return monkey.number
        else:
            return [inner(dictionary[monkey.first]), monkey.function, inner(dictionary[monkey.second])]

    funcs = {
        '*': lambda x, y: int(x * y) if not isinstance(x, list) and not isinstance(y, list) else [x,'*', y],
        '/': lambda x, y: int(x / y) if not isinstance(x, list) and not isinstance(y, list) else [x,'/',y],
        '-': lambda x, y: int(x - y) if not isinstance(x, list) and not isinstance(y, list) else [x,'-',y],
        '+': lambda x, y: int(x + y) if not isinstance(x, list) and not isinstance(y, list) else [x,'+',y]
    }

    def interp_inner(lst):
        if isinstance(lst, list):
            if -1 in lst:
                return lst
            return funcs[lst[1]](interp_inner(lst[0]), interp_inner(lst[2]))
        if isinstance(lst, int):
            return lst


    first, second = [interp_inner(inner(i)) for i in set_equal]
    print(first, '\n', second)

    def eval_inner(first, second):
        # TODO rewrite to work for test cases other than the advent input
        if isinstance(first, int):
            num = first
            lst = second
        else:
            num = second
            lst = first
        while lst:
            if lst[2] == -1:
                return num - interp_inner(lst[0])
            if isinstance(lst[0], int):
                if lst[1] == '/':
                    num = lst[0] / num
                if lst[1] == '*':
                    num /= lst[0]
                if lst[1] == '-':
                    num = -1 * (num - lst[0])
                if lst[1] == '+':
                    num -= lst[0]
                lst = lst[2]
            else:
                if lst[1] == '/':
                    num *= lst[2]
                if lst[1] == '*':
                    num /= lst[2]
                if lst[1] == '-':
                    num += lst[2]
                if lst[1] == '+':
                    num -= lst[2]
                lst = lst[0]

    return eval_inner(first, second)



if __name__ == '__main__':
    fname = 'input21.txt'
    interpret_file(fname)
    total = simul(Monkey.monkey_dict)
    print(total)
    match = find_equals(Monkey.monkey_dict)
    print(match)

# 9244733506137 too high