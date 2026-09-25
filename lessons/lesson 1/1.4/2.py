def seq(amount):
    if amount == 1:
        return ['1 1 3']
    elif amount == 2:
        return ['1 1 2', '2 1 3', '1 2 3']

    beg_sec = seq(amount - 1)



num_of_slice = int(input())

# хз