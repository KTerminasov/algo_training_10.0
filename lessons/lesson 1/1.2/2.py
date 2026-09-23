def postfix(expression):
    stack = []
    actions = '+-*'

    for i in expression:
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

    if len(stack) != 1:
        raise ValueError('Длина стека != 1')

    return stack[0]


def to_postfix(expression):
    res = []
    stack = []

    priority = {
        '*': 2,
        '+': 1,
        '-': 1
    }

    for i in expression:
        if i.isdigit():
            res.append(i)
        elif i in ('+-*'):
            while stack and stack[-1] in '+-*' and priority[stack[-1]] >= priority[i]:
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


def solve(raw_line):
    expr = ' ' + ' '.join(raw_line.split()) + ' '
    parsed_expr = []
    number = ''
 
    for i in range(len(expr) - 1):
        if expr[i].isdigit():
            number += expr[i]
        elif expr[i] == ' ':
            if expr[i - 1].isdigit() and expr[i + 1].isdigit():
                return 'WRONG'
        elif expr[i] in '+-*()':
            if number != '':
                parsed_expr.append(number)
                number = ''
            parsed_expr.append(expr[i])
        else:
            return 'WRONG'
 
    if number != '':
        parsed_expr.append(number)
 
    if not parsed_expr:
        return 'WRONG'
 
    try:
        return str(postfix(to_postfix(parsed_expr)))
    except (IndexError, ValueError, ZeroDivisionError):
        return 'WRONG'


print(solve(input()))
