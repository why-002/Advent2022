points = 0

winning_dict = {'X': ('B', 'A', 'C'), 'Y': ('C', 'B', 'A'), 'Z': ('A', 'C', 'B')}
p_dict = {'X': 1, 'Y': 2, 'Z': 3}

throw_list = []

with open('input2.txt', 'r') as fp:
    for l in fp:
        points += p_dict[l[-2]]

        if winning_dict[l[-2]][0] == l[0]:
            pass
        elif winning_dict[l[-2]][1] == l[0]:
            points += 3
        else:
            points += 6

print(points)
points = 0
with open('input2.txt', 'r') as fp:
    for l in fp:
        if l[-2] == 'X':
            points += 0
            if l[0] == 'A':
                throw_list.append('Z')
            elif l[0] == 'B':
                throw_list.append('X')
            else:
                throw_list.append('Y')

        elif l[-2] == 'Y':
            points += 3
            if l[0] == 'A':
                throw_list.append('X')
            elif l[0] == 'B':
                throw_list.append('Y')
            else:
                throw_list.append('Z')
        else:
            points += 6
            if l[0] == 'A':
                throw_list.append('Y')
            elif l[0] == 'B':
                throw_list.append('Z')
            else:
                throw_list.append('X')
print(throw_list)
for l in throw_list:
    points += p_dict[l]
print(points)