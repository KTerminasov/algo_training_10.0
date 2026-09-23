n = int(input())
songs = []
for i in range(n):
    data = input().split()
    songs.append((data[0], int(data[1])))

m = int(input())
events = []
for i in range(m):
    t, name, length = input().split()
    events.append((int(t), name, int(length)))

first = 0
front = []


def is_empty():
    return first >= n and not front


def pop_front():
    global first
    if front:
        return front.pop()
    song = songs[first]
    first += 1
    return song


total = n + m 
played = 0
cur_end = 0
idx = 0
ans = []

while played < total:
    while idx < m and events[idx][0] <= cur_end:
        t, name, length = events[idx]
        front.append((name, length))
        idx += 1

    if is_empty():
        cur_end = events[idx][0]
        continue

    name, length = pop_front()
    start = cur_end
    ans.append(name + " " + str(start))
    cur_end = start + length
    played += 1

print("\n".join(ans))


