n, m = map(int, input().split())

a = []
for i in range(n):
    a.append(input().split())

res = 0

for i in range((n + 1) // 2):
    for j in range((m + 1) // 2):
        i2 = n - 1 - i
        j2 = m - 1 - j

        coords = {(i, j), (i, j2), (i2, j), (i2, j2)}

        # считаем частоты значений вручную, без Counter
        freq = {}
        for x, y in coords:
            val = a[x][y]
            freq[val] = freq.get(val, 0) + 1

        best = max(freq.values())
        res += len(coords) - best

print(res)