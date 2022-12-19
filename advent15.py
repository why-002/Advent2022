import multiprocessing


def foo(string):
    return string.isdigit() or string == '-'

def in_range(sensor, distance, point):
    x_distance = sensor[0]-point[0]
    y_distance = sensor[1]-point[1]
    if abs(x_distance) + abs(y_distance) <= distance:
        return True
    else:
        return False

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

def find_originals(coordinates: list, abs=abs):
    sensors = []
    beacons = []
    distances = []
    x_pool = []
    for i in coordinates:
        sensors.append([i[0], i[1]])
        beacons.append([i[2], i[3]])
        max_distance = abs(i[0] - i[2]) + abs(i[1] - i[3])
        distances.append(max_distance)
        x_pool.append(i[0] + max_distance)
        x_pool.append(i[0] - max_distance)
    x_pool.sort()
    return sensors, beacons, distances, x_pool

def use_beacons(y_target, sensors,beacons,distances, x_pool, abs=abs):

    no_beacon = []
    for i in range(x_pool[0], x_pool[-1] + 1):
        if [i, y_target] in beacons:
            # print('B', end='')
            pass
        else:
            for k, l in zip(sensors, distances):
                x_movement = abs(i - k[0])
                y_movement = abs(y_target - k[1])
                if l >= x_movement + y_movement:
                    no_beacon.append([i, y_target])
                    # print('#', end='')
                    break
            else:
                # print('.', end='')
                pass
    print()
    return no_beacon


def find_lone_frequency(sensors, distances, min_val, max_val, abs=abs):
    possible = []
    for s, d in zip(sensors, distances):
        for x in range(-d-1, d+2):
            x_coord = s[0] + x
            if min_val <= x_coord <= max_val:
                left_over = abs(d)-abs(x)
                for y in [-left_over-1, left_over+1]:
                    y_coord = s[1] + y
                    if min_val <= y_coord <= max_val:
                        possible.append([x_coord, y_coord])
    return possible


if __name__ == '__main__':
    coordinates = interpret_file('input15.txt')
    originals = find_originals(coordinates)
    #line_ = use_beacons(2000000, originals[0], originals[1], originals[2], originals[3])
    #print(len(line_))
    possible = find_lone_frequency(originals[0], originals[2], 0, 4000000)
    print(possible)
    for i in possible:
        no_beacon = False
        for s, d in zip(originals[0], originals[2]):
            if in_range(s,d,i):
                no_beacon = True
            else:
                pass
        if not no_beacon:
            print(i[0] * 4000000 + i[1])
            break



# 4157653 too low

# 4013449946094 too low part 2
