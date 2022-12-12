with open('input10.txt', 'r') as fp:
    file = fp.readlines()

file = [i.strip().split() for i in file]
print(file)
queue = [0,0]

nums = []
x_count = 1


def do_thing(file, queue, x_count):
    if not file:
        return
    if 'addx' in file[0]:
        file = [file[0][1]] + file[1:]
        nums.append(x_count)

    elif 'noop' in file[0]:
        nums.append(x_count)
        file = file[1:]
    else:
        nums.append(x_count)
        x_count += int(file[0])
        file = file[1:]
    return do_thing(file, queue, x_count)


do_thing(file, queue, x_count)

wanted = [20, 60, 100, 140, 180, 220]
total = 0

print(nums)

for i in wanted:
    print(nums[i-1])
    total += i * nums[i-1]
print(total)

inds = [0,40,80,120,160,200]
for ind in inds:
    for i in range(ind,40+ind):
        if abs(i-ind - nums[i]) < 2:
            print('#', end='')
        else:
            print('.', end='')
    print()


