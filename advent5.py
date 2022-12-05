class Stack:
    def __init__(self):
        self.objects = []

    def __repr__(self):
        return f'{self.objects}'


def original_setup_reader(filename, depth, stacklist):
    with open(filename, 'r') as fp:
        for d in range(depth):
            line = fp.readline()
            line = [i for i in line]
            indexes = [1, 5, 9, 13, 17, 21, 25, 29, 33]
            for index, i in enumerate(indexes):
                if line[i] != ' ':
                    stacklist[index].objects = [line[i]] + stacklist[index].objects

    return stacklist


stacklist = [Stack() for _ in range(9)]
stacklist = original_setup_reader('input5.txt', 8, stacklist)

print(stacklist)


def read_transactions():
    with open('input5.txt', 'r') as fp:
        first_char = ''
        while first_char != 'm':
            line = fp.readline()
            first_char = line[0]
        file = [line] + fp.readlines()
        num_moved, stack_to, stack_from = [], [], []
        for index, i in enumerate(file):

            nums = []
            for char in i:
                if char.isdigit():
                    nums += char
            stack_from.append(int(nums.pop(-2)) - 1)
            stack_to.append(int(nums.pop(-1)) - 1)
            num_moved.append(int(f'{nums[0]}{nums[1]}') if len(nums) > 1 else int(nums[0]))
        return stack_from, stack_to, num_moved


r = read_transactions()
print(r)


def original(stack_from, stack_to, num_moved):
    for _ in range(num_moved):
        stacklist[stack_to].objects.append(stacklist[stack_from].objects.pop())


s = map(original, r[0], r[1], r[2])
list(s)
print(''.join([i.objects[-1] for i in stacklist]))

stacklist2 = [Stack() for _ in range(9)]
stacklist2 = original_setup_reader('input5.txt', 8, stacklist2)


def new(stack_from, stack_to, num_moved):
    for moved in range(num_moved, 0, -1):
        stacklist2[stack_to].objects.append(stacklist2[stack_from].objects.pop(-moved))


s = map(new, r[0], r[1], r[2])
list(s)
print(''.join([i.objects[-1] for i in stacklist2]))
