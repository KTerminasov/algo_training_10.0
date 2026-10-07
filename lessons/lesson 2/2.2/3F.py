from collections import deque

n, k = map(int, input().split())
seq = list(map(int, input().split()))

deq: deque = deque()
for i, x in enumerate(seq):
    while deq and deq[-1] > x:
        deq.pop()

    deq.append(x)

    if i + 1 > k and deq[0] == seq[i - k]:
        deq.popleft()

    if i >= k - 1:
        print(deq[0])
