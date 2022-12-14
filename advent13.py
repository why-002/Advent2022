import json
import sys

sys.setrecursionlimit(1000000000)


def compare(lst1, lst2):
    if lst1 == [] and lst2 == []:
        return None
    if lst1 == []:
        return True
    if lst2 == []:
        return False

    if isinstance(lst1[0], list) and isinstance(lst2[0], list):
        potential_solution = compare(lst1[0], lst2[0])
        if potential_solution is not None:
            return potential_solution
        else: # Test case that was holding me up, didn't have the if conditionals, so I got messed up by other boolean statements
            if len(lst1[0]) < len(lst2[0]):
                return True
            if len(lst1[0]) > len(lst2[0]):
                return False
            return compare(lst1[1:], lst2[1:])

    elif isinstance(lst1[0], int) and isinstance(lst2[0], int):
        if lst1[0] < lst2[0]:
            return True
        elif lst1[0] > lst2[0]:
            return False
        else:
            return compare(lst1[1:], lst2[1:])
    else:
        if isinstance(lst1[0], int):
            return compare([lst1[0]], lst2[0])
        if isinstance(lst2[0], int):
            return compare(lst1[0], [lst2[0]])


def sort(lst):
    final = []
    original = [i for i in lst]
    while original:
        if len(final) == 0:
            final = original.pop(0)
        else:
            if compare(final[-1], original[0]):
                final.append(original.pop(0))
            for index, value in enumerate(final):
                if compare(original[0], value):
                    final = final[:index] + [original.pop(0)] + final[index:]
                    break

    return final


with open('input13.txt', 'r') as fp:
    file = []
    for index, line in enumerate(fp):

        line = line.strip()
        line = line + ',\n'
        if line == ',\n':
            line = '\n'
        if line == '[[[2,3,9,3,[2,8]],6],[2,10],[[[2,10],9,1,5],[6,[],[1,0,2,10,8],5],10],[4]],\n':
            line = '[[[2,3,9,3,[2,8]],6],[2,10],[[[2,10],9,1,5],[6,[],[1,0,2,10,8],5],10],[4]]\n'
        file += [line]

with open('input13.json', 'w') as fp:
    for index, line in enumerate(file):
        if line == file[0]:
            fp.write('[' + line)
        elif line == file[-1]:
            fp.write(line + ']')
        else:
            fp.write(line)

with open('input13.json', 'r') as fp:
    f = json.load(fp)
    print(f)

results = {}
count = 1
part1 = f.copy()
while part1:
    results[count] = compare(part1[0], part1[1])
    part1 = part1[2:]
    count += 1
print(results)

results = [i[0] for i in results.items() if i[1] is True]
print(results)
print(sum(results))
f = sort(f + [[[2]], [[6]]])
print(f)
low = f.index([[2]])+1
high = f.index([[6]])+1
print(high * low)
# 6215 is too low, not 6231
