class Heap:
    def __init__(self, h=[]):
        pass
            
    def __len__(self):
        return len(self.heap)

    def riddling_downup(self):
        pass

    def insert(self, k):
        self.heap.append(k)   
        
        self.riddling_downup() 

    def riddling_updown(self):
        pass

    def extract(self, delete=True):
        res = self.heap[0] if self.heap else None
        if not delete:
            return res

        self.riddling_updown()
        
        return res


class MaxHeap(Heap):
    def __init__(self, h=[]):
        self.heap = h
    
    def riddling_downup(self):
        i = len(self.heap) - 1

        while i != 0 and self.heap[i] > self.heap[(i-1)//2]:
            self.heap[i], self.heap[(i-1)//2] = self.heap[(i-1)//2], self.heap[i]
            i = (i-1)//2

    def riddling_updown(self):
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


class MinHeap(Heap):
    def __init__(self, h=[]):
        self.heap = h
    
    def riddling_downup(self):
        i = len(self.heap) - 1

        while i != 0 and self.heap[i] < self.heap[(i-1)//2]:
            self.heap[i], self.heap[(i-1)//2] = self.heap[(i-1)//2], self.heap[i]
            i = (i-1)//2

    def riddling_updown(self):
        self.heap[0] = self.heap[-1]
        i = 0
        le = len(self.heap) - 1

        while (2*i + 1) <= le and (2*i + 2) <= le:
            if self.heap[2*i + 1] < self.heap[2*i + 2] and self.heap[2*i + 1] < self.heap[i]:
                self.heap[i], self.heap[2*i + 1] = self.heap[2*i + 1], self.heap[i]
                i = 2*i + 1
            elif self.heap[2*i + 2] < self.heap[i]:
                self.heap[i], self.heap[2*i + 2] = self.heap[2*i + 2], self.heap[i]
                i = 2*i + 2
            else:
                break
        
        self.heap.pop()


l_maxheap = MaxHeap()
r_minheap = MinHeap()
ans = []

count = int(input())
for i in map(int, input().split()):
    l_max = l_maxheap.extract(delete=False)
    if len(l_maxheap) == 0 or l_max > i:
        l_maxheap.insert(i)
    else:
        r_minheap.insert(i)
    
    if len(l_maxheap) - len(r_minheap) > 1:
        r_minheap.insert(l_maxheap.extract())
    elif len(l_maxheap) - len(r_minheap) <= -1:
        l_maxheap.insert(r_minheap.extract())
    
    ans.append(l_maxheap.extract(delete=False))

print(' '.join(map(str, ans)))

