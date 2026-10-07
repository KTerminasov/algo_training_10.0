from collections import deque

requests = int(input())

left_deq = deque()
left_size = 0
right_deq = deque()
right_size = 0

ans = []
for i in range(requests):
    req = input().split()
    
    if req[0] == '-':
        if left_deq:
            ans.append(left_deq.popleft())
            left_size -= 1
        else:
            ans.append(right_deq.popleft())
            right_size -= 1
    elif req[0] == '+':
        right_deq.append(req[1])
        right_size += 1
    elif req[0] == '*':
        if (left_size + right_size) % 2 == 1:  # нечётная длина — как раньше
            left_deq.append(right_deq.popleft())
            left_size += 1
            right_deq.appendleft(req[1])
        else:  # чётная длина — просто в середину, без сдвига
            right_deq.appendleft(req[1])
            right_size += 1
    
    if left_size - right_size < -1:
        left_deq.append(right_deq.popleft())
        left_size += 1
        right_size -= 1
    elif left_size - right_size > 1:
        right_deq.appendleft(left_deq.pop())
        left_size -= 1
        right_size += 1

print('\n'.join(ans))