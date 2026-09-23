expr = input().split()

stack = []
actions = '+-*'

for i in expr:
    if i in actions:
        top1 = stack.pop()
        top2 = stack.pop()
        res = 0

        if i == '+':
            res = top1 + top2
        elif i == '-':
            res = top2 - top1
        else:
            res = top1 * top2
        
        stack.append(res)
    else:
        stack.append(int(i))

print(*stack)