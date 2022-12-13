import random
import sys
import multiprocessing
from functools import cache
import os
import time
from turtle import Turtle

class Hill:
    def __init__(self, height, x, y):
        self.height = height
        self.x = int(x)
        self.y = int(y)

    def __repr__(self):
        return str(self.height)

'''t = Turtle()
t.pencolor('blue')
t.speed(0)'''

def walk(starting, file, depth, prev):
    #t.goto(starting.x,starting.y)
    if prev is None:
        prev = []
    if starting.height == -14:
        starting.height = 0
    depth = depth + 1
    try:
        if depth >= min(walks.values()):
            return
    except ValueError:
        pass

    dirs = []

    try:
        right = file[starting.y][starting.x + 1]
        dirs.append(right)
    except:
        pass

    try:
        down = file[starting.y + 1][starting.x]
        dirs.append(down)
    except:
        pass

    try:
        assert starting.y > 0
        up = file[starting.y - 1][starting.x]
        dirs.append(up)
    except:
        pass

    try:
        assert starting.x > 0
        left = file[starting.y][starting.x - 1]
        dirs.append(left)
    except:
        pass

    directions = []

    for direction in dirs:
        if direction.height > starting.height + 1:
            pass
        elif direction in golden_path:
            directions += [direction]
        elif direction in dead_end:
            pass
        elif direction.height == 0 and depth > 2:
            dead_end.add(direction)
        elif direction in prev:
            pass
        else:
            directions += [direction]

    dirs = directions


    for direction in dirs:

        if direction == final:
            walks[len(walks) + 1] = depth
            print(f'Success at {depth}')
            golden_path.add(direction)
            golden_path.add(starting)
            return True

        else:
            p = prev.copy()
            p.append(starting)
            w = walk(direction, file, depth, p)
            if w is True:
                golden_path.add(starting)

    if len(set(dirs).intersection(dead_end)) == len(dirs) and len(dirs) > 0:
        dead_end.add(starting)

    if not dirs:
        dead_end.add(starting)

if __name__ == '__main__':
    sys.setrecursionlimit(2000000000)

    with open('input12.txt', 'r') as fp:
        file = []
        for index, line in enumerate(fp):
            line = line.strip()
            line = [Hill(ord(value) - 97, i, index) for i, value in enumerate(line)]
            file += [line]
    walks = {}
    depth_count = []
    dead_end = set()
    golden_path = set()

    final = ''
    for line in file:
        for i in line:
            if i.height == -28:
                final = i
                i.height = 25
                print(final)
    walk(file[20][0], file, 0, None)
    print(walks)
    success = [i for i in walks.values()]
    success.sort()
    print(success[0])
    print(dead_end)

#less than 2039, less than 1829, less than 1011, not 906, not 806, not 810