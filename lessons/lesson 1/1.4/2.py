def move(n, fr, to):
    'Перенос n дисков с стержня fr на стержень to'

    if n == 0:
        return

    move(n - 1, fr, 6 - fr - to)
    print(n, fr, to)
    move(n - 1, 6 - fr - to, to)


num_of_slice = int(input())
move(num_of_slice, 1, 3)
