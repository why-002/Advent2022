class Rope:

    def __init__(self, x=0, y=0):
        self.h = [x,y]
        self.t = [x,y]
        self.t_log = [self.t.copy()]
        self.h_log = [self.h.copy()]

    def update_t(self):

        if abs(self.h[0]-self.t[0]) < 1 and abs(self.h[1]-self.t[1]) < 1:
            return

        for coord in range(2):

            if abs(self.h[coord] - self.t[coord]) == 2:
                self.t[coord] += -1 if self.h[coord] - self.t[coord] < 0 else 1
                opposite = (coord-1) * -1
                if self.t[opposite] != self.h[opposite]:        # checks the other option
                    self.t[opposite] = self.h[opposite]
        self.t_log.append(self.t.copy())




    def move(self, move_dir, num):

        move_dict = {'R': (0, 1), 'L': (0, -1), 'U': (1, 1), 'D': (1, -1)}

        ind, dir = move_dict[move_dir]
        for i in range(num):
            self.h[ind] += (1 * dir)
            self.update_t()
            self.h_log.append(self.h.copy())
        return



with open('input9.txt', 'r') as fp:
    file = fp.readlines()

# coordinates x,y
r = Rope()
for i in file:
    print(i)
    dir, num = i.split(' ')
    r.move(dir,int(num))

print(r.t_log)

new_log = []

for i in r.t_log:
    if i not in new_log:
        new_log.append(i)
    else:
        pass
print(len(new_log))