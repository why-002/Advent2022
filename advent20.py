import sys

sys.setrecursionlimit(10 ** 6)


def intepret_file(fname: str):
    with open(fname, 'r') as fp:
        codes = []
        for line in fp:
            line = int(line.strip())
            codes.append(line)
    return codes


class CircularList:
    def __init__(self, nodes):
        self.nodes = nodes

    def __getitem__(self, key):
        length = len(self.nodes)
        if isinstance(key, slice):
            return CircularList(self.nodes[key])
        if key > length - 1:
            return self.__getitem__(key - length)
        elif key < -length:
            return self.__getitem__(key + length)
        else:
            return self.nodes[key]

    def __setitem__(self, key, value):
        self.nodes[key] = value

    def __repr__(self):
        return str(self.nodes)

    def __add__(self, other):
        return CircularList(self.nodes + other.nodes)

    def pop(self, key):
        return self.nodes.pop(key)

    def index(self, value):
        for index, val in enumerate(self.nodes):
            if val == value:
                return index


def re_order(original_list, new_list):
    print(new_list)
    for index, value in enumerate(original_list):
        current_index = new_list.index(value)
        if value >= 0:
            new_list = new_list[:current_index + value + 1] + CircularList([value]) + new_list[current_index + value + 1:]
        elif current_index + value == 0:
            new_list = new_list[:] + CircularList([value])
        else:
            new_list = new_list[:current_index + value] + CircularList([value]) + new_list[current_index + value:]
        if value < 0 and current_index - value > 1 or value + current_index > len(original_list):
            new_list.pop(current_index)
        else:
            new_list.pop(current_index)
        print(new_list)
    return new_list


if __name__ == '__main__':
    file_name = 'test20.txt'
    codes = intepret_file(file_name)
    c = CircularList(codes)
    n = CircularList(codes)
    print(re_order(codes, c))
# 12629 too high, 10719 too low
