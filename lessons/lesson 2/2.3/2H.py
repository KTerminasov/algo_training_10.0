import heapq

n, w = map(int, input().split())

blocks = []
for i in range(n):
    pos_i, w_i = map(int, input().split())
    blocks.append((pos_i, w_i, i+1))
blocks.sort(key=lambda x: x[0])

rows = []
ans = []

for pos_i, w_i, num in blocks:
    right = pos_i + w_i

    if rows and rows[0][0] <= pos_i:
        _, num_row = heapq.heappop(rows)
        ans[num_row].append(num)
        heapq.heappush(rows, (right, num_row))
    else:
        num_row = len(ans)
        ans.append([num]) 
        heapq.heappush(rows, (right, num_row))

res = []
for i in ans:
    res.extend(i)

print(len(ans))        
print(*(res))


