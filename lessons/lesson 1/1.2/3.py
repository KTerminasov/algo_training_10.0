def to_postfix(expression):
    res = []
    stack = []

    priority = {
        '!': 3,
        '&': 2,
        '|': 1,
        '^': 1
    }
    operations = priority.keys()

    for i in expression:
        if i.isdigit():
            res.append(i)
        elif i in operations:
            while stack and stack[-1] in operations and priority[stack[-1]] >= priority[i]:
                res.append(stack.pop())
            stack.append(i)
        elif i == '(':
            stack.append(i)
        elif i == ')':
            while stack[-1] != '(':
                res.append(stack.pop())
            stack.pop()

    res += reversed(stack)
    return res


def postfix(expression):
    stack = []
    actions = '!&|^'

    for i in expression:
        if i in actions:
            top1 = stack.pop()
            res = 0

            if i == '!':
                res = int(not top1)
            else:
                top2 = stack.pop()

                if i == '&':
                    res = top1 & top2
                elif i == '^':
                    res = top2 ^ top1
                else:
                    res = top2 | top1
                
            stack.append(res)
        else:
            stack.append(int(i))

    if len(stack) != 1:
        raise ValueError('Длина стека != 1')

    return stack[0]


exp = input()
print(postfix(to_postfix(exp)))
