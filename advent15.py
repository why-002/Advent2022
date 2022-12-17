def foo(string):
    return string.isdigit() or string == '-'
def interpret_file(fname: str):
    with open(fname, 'r') as fp:
        file = []

        for line in fp:
            line = line.strip().split('=')
            line = line[1:]
            for index, value in enumerate(line):
                # noinspection PyTypeChecker
                line[index] = int(''.join(filter(foo, value)))

            file.append(line)
    return file


def use_beacons(coordinates: list, y_target):
    sensors = []
    beacons = []
    distances = []
    x_pool = []
    for i in coordinates:
        sensors.append([i[0], i[1]])
        beacons.append([i[2], i[3]])
        max_distance = abs(i[0]-i[2])+abs(i[1]-i[3])
        distances.append(max_distance)
        x_pool.append(i[0] + max_distance)
        x_pool.append(i[0] - max_distance)

    x_pool.sort()
    no_beacon = []
    for i in range(x_pool[0], x_pool[-1] + 1):
        if [i, y_target] in beacons:
            #print('B', end='')
            pass
        else:
            for k, l in zip(sensors, distances):
                x_movement = abs(i - k[0])
                if l - x_movement >= abs(y_target - k[1]):
                    no_beacon.append(i)
                    #print('#', end='')
                    break
            else:
                #print('.', end='')
                pass
    print()
    return no_beacon

def find_lone_frequency(coordinates: list, y_max, x_max):
    sensors = []
    beacons = []
    distances = []
    x_pool = []
    for i in coordinates:
        sensors.append([i[0], i[1]])
        beacons.append([i[2], i[3]])
        max_distance = abs(i[0] - i[2]) + abs(i[1] - i[3])
        distances.append(max_distance)
        no = []
    print(sensors)
    print(beacons)
    print(distances)
    for x in range(x_max+1):
        for y in range(y_max+1):
            if [x , y] in beacons:
                # print('B', end='')
                no.append([x, y])
            else:
                for k, l in zip(sensors, distances):
                    x_movement = abs(x - k[0])
                    if (l - x_movement >= abs(y - k[1])):
                        no.append([x, y])
    print(no)
    for x in range(x_max+1):
        for y in range(y_max+1):
            if [x, y] not in no and [x, y] not in beacons:
                print(x,y)
                return x * 4000000 + y




if __name__ == '__main__':
    coordinates = interpret_file('input15.txt')
    print(len(use_beacons(coordinates, 2000000)))
    print(find_lone_frequency(coordinates, 4000000, 4000000))
# 4157653 too low

# 4013449946094 too low part 2
