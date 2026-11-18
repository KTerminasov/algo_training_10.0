def merge(first, second):
    n = len(first)
    m = len(second) 
    res = []
    p1 = 0
    p2 = 0

    invertions = 0

    for _ in range(n + m):
        if p1 < n and (p2 >= m or first[p1] <= second[p2]):
            res.append(first[p1])
            p1 += 1
        else:
            res.append(second[p2])
            p2 += 1
            invertions += n - p1

    return (res, invertions)


def merge_sort(a):
    ln = len(a)

    if ln <= 1:
        return (a, 0)

    l, num_l = merge_sort(a[:ln//2])
    r, num_r = merge_sort(a[ln//2:])
    res, num_cross = merge(l, r)

    num_all = num_l + num_r + num_cross

    return (res, num_all)


n = int(input())
arr = list(map(int, input().split()))

print(merge_sort(arr)[1])



