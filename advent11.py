class Monkey:
    monkey_list = []

    def __init__(self, name: str):
        Monkey.monkey_list.append(self)
        self.name = name.lower()
        self.items = []
        self.operation = None
        self.operation_value = None
        self.test = 0
        self.passed = 0
        self.failed = 0
        self.choices = {'+': lambda x, y: x + y, '*': lambda x, y: x * y}
        self.inspect_log = 0

    def __lt__(self, other):
        return self.inspect_log < other.inspect_log

    def __repr__(self):
        return f'{self.inspect_log}'

    def pass_to_monkey(self):
        while self.items:
            if self.items[0] % self.test == 0:
                for i in Monkey.monkey_list:
                    if str(self.passed) in i.name:
                        i.items.append(self.items.pop(0))
            else:
                for i in Monkey.monkey_list:
                    if str(self.failed) in i.name:
                        i.items.append(self.items.pop(0))

    def inspect(self):
        new_items = []
        for item in self.items:
            self.inspect_log += 1
            if isinstance(self.operation_value, str):
                item = self.choices[self.operation](item, item)
                new_items.append(item)
            else:
                item = self.choices[self.operation](item, self.operation_value)
                new_items.append(item)
        self.items = new_items


with open('input11.txt', 'r') as fp:
    for line in fp:
        if 'Monkey' in line:
            new_monkey = Monkey(line.strip())

            items = fp.readline().strip().split(':')
            items = items[1].strip().split(', ')
            items = map(int, items)
            new_monkey.items = list(items)

            operation = fp.readline().strip().split(' ')
            new_monkey.operation = operation[-2]
            new_monkey.operation_value = int(operation[-1]) if operation[-1].isdigit() else operation[-1]

            test = fp.readline().strip().split()[-1]
            new_monkey.test = int(test)

            passed = fp.readline().strip().split()[-1]
            new_monkey.passed = int(passed)

            failed = fp.readline().strip().split()[-1]
            new_monkey.failed = int(failed)

for index in range(10000):
    print(index)
    for i in Monkey.monkey_list:
        i.inspect()
        i.pass_to_monkey()
print(Monkey.monkey_list)
print([i.items for i in Monkey.monkey_list])
Monkey.monkey_list.sort()
print(Monkey.monkey_list[-1].inspect_log*Monkey.monkey_list[-2].inspect_log)
