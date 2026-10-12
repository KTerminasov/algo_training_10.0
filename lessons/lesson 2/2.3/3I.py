import heapq

n = int(input())
nums = input().split()
heap = []

for num in nums:
    heapq.heappush(heap, int(num))

tax = 0
while len(heap) > 1:
    cur_sum = heapq.heappop(heap) + heapq.heappop(heap)
    tax += cur_sum * 0.05
    heapq.heappush(heap, cur_sum)

print(f'{tax:.2f}')
