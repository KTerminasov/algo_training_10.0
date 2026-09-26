first = list(map(int, input().split()))
second = list(map(int, input().split()))

stop = False
moves = 0
while not stop:
    first_card = first.pop(0)
    second_card = second.pop(0)

    if first_card in (0, 9) and second_card in (0, 9):
        if first_card > second_card:
            second += [first_card, second_card]
        else:
            first += [first_card, second_card]
    elif first_card > second_card:
        first += [first_card, second_card]
    else:
        second += [first_card, second_card]

    moves += 1

    if not first:
        print(f'second {moves}')
        stop = True
    elif not second:
        print(f'first {moves}')
        stop = True
    elif moves == 10**6:
        print('botva')
        stop = True
