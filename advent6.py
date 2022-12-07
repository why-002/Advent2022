with open('input6.txt', 'r') as fp:
    file = fp.readlines()
    file = file[0]


def is_unique(string):
    return len({i for i in string}) == len(string)


def find_start(file, num):
    for index, char in enumerate(file):
        potential_key = file[index:index + num]
        if is_unique(potential_key):
            return index + num


print(find_start(file, 4))
print(find_start(file, 14))
