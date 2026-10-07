class Heap:
    def __init__(self):
        self.heap = []

    def insert(self, k):
        self.heap.append(k)
        i = len(self.heap) - 1
             
        while i != 0 and self.heap[i] > self.heap[(i-1)//2]:
            self.heap[i], self.heap[(i-1)//2] = self.heap[(i-1)//2], self.heap[i]
            i = (i-1)//2

    def extract(self):
        res = self.heap[0]
        self.heap[0] = self.heap[-1]
        i = 0
        le = len(self.heap) - 1

        while (2*i + 1) <= le and (2*i + 2) <= le:
            if self.heap[2*i + 1] > self.heap[2*i + 2] and self.heap[2*i + 1] > self.heap[i]:
                self.heap[i], self.heap[2*i + 1] = self.heap[2*i + 1], self.heap[i]
                i = 2*i + 1
            elif self.heap[2*i + 2] > self.heap[i]:
                self.heap[i], self.heap[2*i + 2] = self.heap[2*i + 2], self.heap[i]
                i = 2*i + 2
            else:
                break

        self.heap.pop()          
        
        return res


n = int(input())
h = Heap()
ans = []

for i in range(n):    

    inp = list(map(int, input().split()))
    if inp[0] == 0:
        h.insert(inp[1])
    else:
        ans.append(f'{h.extract()}\n')

print(''.join(ans))