import sys
sys.setrecursionlimit(1 << 25)

INSERTION_THRESHOLD = 16
MAX_DEPTH = 64          # примерно 2 * log2(10^9)

def insertion_sort(a, left, right):
    for i in range(left + 1, right):
        key = a[i]
        j = i - 1
        while j >= left and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key

def median_of_three(a, left, right):
    mid = (left + right) // 2
    # Сортируем a[left], a[mid], a[right-1]
    if a[mid] < a[left]:
        a[left], a[mid] = a[mid], a[left]
    if a[right - 1] < a[left]:
        a[left], a[right - 1] = a[right - 1], a[left]
    if a[right - 1] < a[mid]:
        a[mid], a[right - 1] = a[right - 1], a[mid]
    # Медиана теперь в mid. Переносим её в конец для удобства (но не обязательно)
    return a[mid]

def partition(a, x, left, right):
    e = g = n = left
    while n < right:
        if a[n] > x:
            n += 1
        elif a[n] == x:
            a[g], a[n] = a[n], a[g]
            g += 1
            n += 1
        else:
            temp = a[n]
            a[n] = a[g]
            a[g] = a[e]
            a[e] = temp
            e += 1
            g += 1
            n += 1
    return e, g

def quicksort(a, left, right, depth=0):
    while right - left > INSERTION_THRESHOLD:
        if depth > MAX_DEPTH:
            # Защита от квадратичного случая — переключаемся на Timsort
            a[left:right] = sorted(a[left:right])
            return

        x = median_of_three(a, left, right)
        equal, greater = partition(a, x, left, right)

        # Сначала меньшая часть
        if equal - left < right - greater:
            quicksort(a, left, equal, depth + 1)
            left = greater
        else:
            quicksort(a, greater, right, depth + 1)
            right = equal

        depth += 1

    # Маленький кусок — insertion sort
    if right - left > 1:
        insertion_sort(a, left, right)

n = int(input())
if n > 0:
    arr = list(map(int, input().split()))
    quicksort(arr, 0, n)
    print(*arr)