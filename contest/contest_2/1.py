n, k = map(int, input().split())
digits = list(map(int, input().split()))

repeats = {}
for i in digits:
    repeats[i] = repeats.get(i, 0) + 1

res = 0
seen = set()

for digit in repeats:
    if digit not in seen:
        other = k - digit
        
        if digit == other:
            res += max(0, repeats[digit] - 1)
        elif other in repeats:
            res += min(repeats[digit], repeats[other])
            seen.add(other)
        
        seen.add(digit)

print(res)
            
    


