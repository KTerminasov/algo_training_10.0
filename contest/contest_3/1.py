n, m = map(int, input().split())

grid = []
st = []

for i in range(n):
    s = input()
    grid.append(s)

    length = 0
    runs = []
    for j in range(m):
        if s[j] == '#':
            length += 1
        else:
            if length > 0:
                runs.append(length)
            length = 0
    if length > 0:
        runs.append(length)

    st.append([len(runs), runs])

col = []

for j in range(m):
    length = 0
    runs = []
    for i in range(n):
        if grid[i][j] == '#':
            length += 1
        else:
            if length > 0:
                runs.append(length)
            length = 0
    if length > 0:
        runs.append(length)

    col.append([len(runs), runs])

for cnt, runs in st:
    print(cnt, *runs)

for cnt, runs in col:
    print(cnt, *runs)
