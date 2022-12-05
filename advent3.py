paired = []

with open('input3.txt', 'r') as fp:
    for line in fp:
        length = len(line)
        c1, c2 = line[:int(length/2)], line[int(length/2):]
        short_list = []
        for i in c1:
            if i in c2:
                short_list.append(i)
        short_list = set(short_list)
        for i in short_list:
            paired.append(i)

paired.sort()

print(paired)

sp = paired.index('b')

upper, lower = paired[:sp], paired[sp:]

print(upper)
print(ord('A'))
print(lower)
print(ord('a'))

lower = [ord(i)-96 for i in lower]
upper = [ord(i)-38 for i in upper]

print(upper)
print(lower)

print(sum(upper) + sum(lower))

def find_badge(lst):
    if not lst:
        return []
    else:
        use,pass_on = lst[:3], lst[3:]
        formatted_use = []
        for i in use:
            i = i.strip()
            formatted_use += [i]
        badge = set(formatted_use[0]).intersection(set(formatted_use[1])).intersection(set(formatted_use[2]))
        badge = badge.pop()
        return [badge] + find_badge(pass_on)




with open('input3.txt', 'r') as fp:
    lst = fp.readlines()
    print(lst)
    lst = find_badge(lst)
    print(lst)
    lst.sort()
    print(lst)

sp = lst.index('b')

upper, lower = lst[:sp], lst[sp:]

lower = [ord(i)-96 for i in lower]
upper = [ord(i)-38 for i in upper]
print(sum(upper) + sum(lower))