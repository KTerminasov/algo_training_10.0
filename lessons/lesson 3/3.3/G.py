def merge(first, second):
    n = len(first)
    m = len(second) 
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


def merge_sort(a):
    ln = len(a)

    if ln <= 1:
        return a

    return merge(merge_sort(a[:ln//2]), merge_sort(a[ln//2:]))


n = int(input())
arr = list(map(int, input().split()))

print(*merge_sort(arr))



