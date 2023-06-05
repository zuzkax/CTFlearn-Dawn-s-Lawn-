r = open("Lawn2", "r")

lawn = []


for line in r:
    line = line.strip()
    row = []
    for tile in line:
        row.append(tile)
    lawn.append(row)

print(lawn)
states1 = {
    '.': 0,
    '_': 1,
    '\\': 2,
    '-': 3,
    '/': 4,
    '|': 5,
    '*': 6
}

states2 = {
    0: '.',
    1: '_',
    2: '\\',
    3: '-',
    4: '/',
    5: '|',
    6: '*'
}
#mowing
i = 0
while i < len(lawn):
    for j in range(len(lawn)):
        print(j, i)
        old = states1[lawn[j][i]]
        new = old - 2
        print(new)
        if new < 0:
            lawn[j][i] = '.'
        else:
            lawn[j][i] = states2[new]
    i += 1


#regrowth
tiles = len(lawn)**2
print(lawn)
i = 0
while i < len(lawn):
    for j in range(len(lawn)):
         if lawn[j][i] != '.':
             u = (tiles - 1) // len(lawn)
             #print(u)
             tiles -= 1
             if (states1[lawn[j][i]]) + u > 6:
                 lawn[j][i] = '*'
             else:
                 lawn[j][i] = states1[lawn[j][i]] + u
                 lawn[j][i] = states2[lawn[j][i]]

         else:
             tiles -= 1
             #print("infertile dirt")
         #print('tiles:' + ' ', tiles)
    i += 1

print(lawn)

# flower counter
counter = 0
for row in lawn:
    for tile in row:
        if tile == '*':
            counter += 1

print(counter)
