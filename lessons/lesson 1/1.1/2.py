n = int(input())
w = input()
s = input()

stack = []
remain = n - len(s)
res = []
pairs = {
    ')': '(',
    ']': '['
}

for i in s:
    if i in ('(', '['):
        stack.append(i)
    else:
        stack.pop()

for i in range(remain):
    cur_remain = remain - i

    for w_i in w:
        if w_i in ('(', '[') and cur_remain - 1 >= len(stack) + 1 and (cur_remain - 1 - (len(stack) + 1)) % 2 == 0:
            stack.append(w_i)
            res += w_i
            break
        elif stack and w_i in (')', ']') and pairs[w_i] == stack[-1]:
            if cur_remain - 1 >= len(stack) - 1 and (cur_remain - 1 - (len(stack) - 1)) % 2 == 0:
                stack.pop()
                res += w_i
                break

print(s+''.join(res))    