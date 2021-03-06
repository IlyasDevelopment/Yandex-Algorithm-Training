def makefield(n, m, mines):
    di = (-1, -1, -1,  0, 0,  1, 1, 1)
    dj = (-1,  0,  1, -1, 1, -1, 0, 1)
    field = []
    for k in range(n + 2):
        field.append([0] * (m + 2))
    for minei, minej in mines:
        for k in range(len(di)):
            field[minei + di[k]][minej + dj[k]] += 1
    for minei, minej in mines:
        field[minei][minej] = '*'
    return field


n, m, k = map(int, input().split())
mines = []
for i in range(k):
    mines.append(tuple(map(int, input().split())))
field = makefield(n, m, mines)
for i in range(1, n + 1):
    for j in range(1, m + 1):
        print(field[i][j], end=' ')
    print()
