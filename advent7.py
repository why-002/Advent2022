from functools import cache

nums = []


class File:
    file_dict = []

    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.owner = None
        File.file_dict.append(self)

    def get_size(self):
        return self.size

    def __repr__(self):
        return f'{self.name}'


class Directory:
    dir_list = []

    def __init__(self, name):
        self.name = name
        self.size = None
        self.objects = []
        Directory.dir_list.append(self)
        self.owner = None

    def add_file(self, obj):
        self.objects.append(obj)
        obj.owner = self

    def __repr__(self):
        return f'{self.name}'

    @cache
    def get_size(self):
        sum_size = 0
        for i in self.objects:
            sum_size += i.get_size()
        return sum_size


with open('input7.txt', 'r') as fp:
    set_dir = Directory('/')
    for line in fp:
        line = line.strip().split(' ')
        if line[0] == '$':
            if line[1] == 'cd':
                if line[-1] == '..':
                    set_dir = set_dir.owner
                elif line[-1] in Directory.dir_list:
                    set_dir = Directory.dir_list[line[-1]]
                else:
                    set_dir.add_file(Directory(line[-1]))
                    set_dir = set_dir.objects[-1]
            elif 'ls' in line:
                pass
        else:
            if line[0] == 'dir':
                set_dir.add_file(Directory(line[-1]))
            else:
                set_dir.add_file(File(line[1], int(line[0])))

total = [i.get_size() for i in Directory.dir_list if i.get_size() <= 100000]
print(sum(total))