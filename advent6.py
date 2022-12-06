with open('input6.txt', 'r') as fp:
    file = fp.readlines()
    file = file[0]


def is_unique(string):
    return len({i for i in string}) == len(string)


def find_key(file):
    for index, char in enumerate(file):
        potential_key = file[index:index + 4]
        for i in potential_key:
            if is_unique(potential_key):
                return index+4

def find_start_of_message(file):
    for index, char in enumerate(file):
        potential_key = file[index:index + 14]
        for i in potential_key:
            if is_unique(potential_key):
                return index+14


print(find_key(file))
print(find_start_of_message(file))
