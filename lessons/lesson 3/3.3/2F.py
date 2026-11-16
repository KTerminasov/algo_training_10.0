outfits = []
for i in range(4):
    input()
    outfits.append(sorted((map(int, input().split()))))

pointers = [0] * len(outfits)
best_outfit = []
min_diff = float('inf')

while all(pointers[i] < len(outfits[i]) for i in range(len(outfits))):
    current_outfit = [outfits[i][pointers[i]] for i in range(len(outfits))]
    min_color = min(current_outfit)
    diff = max(current_outfit) - min_color
    pointers[current_outfit.index(min_color)] += 1

    if diff < min_diff:
        min_diff = diff
        best_outfit = current_outfit
    
    if diff == 0:
        break

print(*best_outfit)