# Количество призеров <= 25% от всех
# Должно быть >= 50 баллов
# У всех участников с одинаковым баллом одинаковый статус
# Определить мин балл для призового места

# i: 00 01 02 03 04 05 06 07
# p: 30 40 40 45 45 45 45 48
# n = 8, quater = 8 // 4 = 2
# curr = n - quater = 8 - 2 = 6
# points[6] == points[6 - 1] = 45 => curr += 1
# points[7] != points[6] => ans = points[7] = 48

# Крайние случаи: все одинаковые - нет призера
# 80 80 80 80 80 -> 81
# 40 40 40 40 40 -> 50

# Нечетное количество участников
# i: 00 01 02 03 04 05 06
# p: 30 40 40 45 50 66 95
# n = 7, quater = 7 // 4 = 1
# res = 95

# что делать, если n < 4?

def min_point(points):
    points.sort()
    n = len(points)
    quater = n // 4  # Мб округлять вниз

    curr = n - quater
    while curr < n - 1:
        if points[curr] != points[curr - 1] and points[curr] >= 50:
            return points[curr]           
        else:
            curr += 1

    return max(50, points[-1] + 1)


points = list(map(int, input().split()))
print(min_point(points))

