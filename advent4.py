with open("input4.txt", 'r') as fp:
    count = 0
    for line in fp:
        ij, kl = line.split(',')
        i, j = ij.split('-')
        k, l = kl.split('-')
        if int(i) <= int(k) <= int(l) <= int(j):
            count += 1
        elif int(k) <= int(i) <= int(j) <= int(l):
            count += 1
print(count)


with open("input4.txt", 'r') as fp:
    count = 0
    for line in fp:
        ij, kl = line.split(',')
        i, j = ij.split('-')
        k, l = kl.split('-')
        if int(i) <= int(k) <= int(j):
            count += 1
        elif int(k) <= int(i) <= int(l):
            count += 1
print(count)

