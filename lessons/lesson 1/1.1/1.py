seq = input()

stack = []
res = 'yes'
pairs = {
    ')': '(',
    '}': '{',
    ']': '['
}

for i in seq:
    if i in ('(', '{', '['):
        stack.append(i)
    else:
        if not stack or stack.pop() != pairs[i]:
            res = 'no'
            break

if len(stack) != 0:
    res = 'no'

print(res)