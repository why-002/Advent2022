with open('input.txt', 'r') as fp:
    f = fp.readlines()

elf_dict = {}
n = 0
for i in f:
    if i == '\n':
        n += 1
    else:
        i = int(i.strip())
        try:
            elf_dict[n] += [i]
        except KeyError:
            elf_dict[n] = [i]
for i,v in elf_dict.items():
    elf_dict[i] = sum(v)
print(elf_dict)

elf = [i for i in elf_dict.values()]
elf.sort()
print(sum(elf[:-4:-1]))
