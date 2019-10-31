l = open(u'input.txt', 'r+').read().lower().split()
p = open(u'output.txt', 'w')
max_a = 0
prev_max = 0
for i in range(len(l)):
    for j in range(len(l[i])):
        if j == len(l[i]) - 1:
            if l[i][j] == 'a':
                max_a +=1
            if max_a > prev_max:
                prev_max = max_a
            max_a = 0
            continue
        if l[i][j] == "a" and l[i][j + 1] == "a":
            max_a += 1
        elif l[i][j] == "a" and l[i][j + 1] != "a":
            max_a += 1
            if max_a > prev_max:
                prev_max = max_a
            max_a = 0
p.write(str(prev_max))