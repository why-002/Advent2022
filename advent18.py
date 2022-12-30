def interpret_file(fname):
    with open(fname, 'r') as fp:
        blocks = []
        total_sides = 0
        for line in fp:
            line = line.strip().split(',')
            line = (int(i) for i in line)
            line = tuple(line)
            sides = 6
            for b in blocks:
                x_match = b[0] == line[0]
                y_match = b[1] == line[1]
                z_match = b[2] == line[2]
                matches = [x_match,y_match,z_match]
                if matches.count(True) == 2 and b != line:
                    if x_match is False and abs(b[0]-line[0]) == 1:
                        sides -= 1
                        total_sides -= 1
                    elif y_match is False and abs(b[1]-line[1]) == 1:
                        sides -= 1
                        total_sides -= 1
                    elif z_match is False and abs(b[2]-line[2]) == 1:
                        sides -= 1
                        total_sides -= 1
            total_sides += sides
            blocks.append(line)
    return total_sides

if __name__ == '__main__':
    print(interpret_file('input18.txt'))
