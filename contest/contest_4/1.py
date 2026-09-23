x, y = map(int, input().split())

if x > y:
    x, y = y, x
res = 0

while x != 0:
    if x == y:
        res += 1
        break
    
    q = y // x
    r = y % x

    res += q
    if r == 0:
        break

    y, x = x, r

print(res)