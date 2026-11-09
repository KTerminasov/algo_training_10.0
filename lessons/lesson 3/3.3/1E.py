def merge(n, first, m, second):
    res = []
    p1 = 0
    p2 = 0

    for _ in range(n + m):
        if p1 < n and (p2 >= m or first[p1] <= second[p2]):
            res.append(first[p1])
            p1 += 1
        else:
            res.append(second[p2])
            p2 += 1
    
    return res


n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

merged = merge(n, a, m, b)
print(*merged)

