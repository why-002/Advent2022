class Rope:

    def __init__(self, x=0, y=0, one_after = None):
        self.h = [x, y]
        self.t = [x, y]
        self.t_log = [self.t.copy()]
        self.h_log = [self.h.copy()]
        self.one_after = one_after

    def update_t(self):
        x_value_check = abs(self.h[0] - self.t[0]) > 1
        y_value_check = abs(self.h[1] - self.t[1]) > 1
        x_dir = self.h[0] > self.t[0]
        y_dir = self.h[1] > self.t[1]

        if not x_value_check and not y_value_check:
            self.t_log += [self.t.copy()]
            return

        if x_value_check and y_value_check:
            self.t[0] += 1 if x_dir else -1
            self.t[1] += 1 if y_dir else -1
            self.t_log += [self.t.copy()]
            return

        if x_value_check:
            self.t[0] += 1 if x_dir else -1
            if self.t[1] != self.h[1]:
                self.t[1] = self.h[1]

        if y_value_check:
            self.t[1] += 1 if y_dir else -1
            if self.t[0] != self.h[0]:
                self.t[0] = self.h[0]

        self.t_log += [self.t.copy()]

    def move(self, move_dir):

        move_dict = {'R': (0, 1), 'L': (0, -1), 'U': (1, 1), 'D': (1, -1)}

        ind, dir = move_dict[move_dir]
        self.h[ind] += (1 * dir)
        self.h_log.append(self.h.copy())
        self.update_t()


with open('input9.txt', 'r') as fp:
    file = fp.readlines()

# coordinates x,y
r = Rope()
for i in file:
    i = i.strip()
    dir, num = i.split(' ')
    for n in range(int(num)):
        r.move(dir)
new_log = []

for i in r.t_log:
    if i not in new_log:
        new_log.append(i)
    else:
        pass
print(len(new_log))

def new_rope(rope_1, rope_2):
    for i in rope_1.t_log:
        rope_2.h = i
        rope_2.update_t()

one = Rope()
two = Rope()
three = Rope()
four = Rope()
five = Rope()
six = Rope()
seven = Rope()
tail = Rope()


rope_list = [r,one,two,three,four,five,six,seven,tail]
for index, rope in enumerate(rope_list):
    if index == 0:
       pass
    else:
        new_rope(rope_list[index-1], rope)

new_log = []

for i in rope_list[-1].t_log:
    if i not in new_log:
        new_log.append(i)
    else:
        pass
print(len(new_log))