from collections import deque

n = int(input())
powers = deque(map(int, input().split()))
q = int(input())
numbers = [int(input()) for i in range(q)]

# Играем ТОЛЬКО первые n-1 игр по-настоящему.
# К этому моменту самая сильная команда гарантированно уже сыграла
# хотя бы раз и с этого момента будет выигрывать всегда,
# а значит дальше соперники идут по кругу с периодом n-1.
first_games = {}
champion = powers.popleft()
num_games = n - 1

for game in range(1, num_games + 1):
    challenger = powers.popleft()
    first_games[game] = (champion, challenger)
    if champion > challenger:
        powers.append(challenger)
    else:
        powers.append(champion)
        champion = challenger

powers_after = list(powers)
ans = []
for k in numbers:
    if k <= num_games:
        a, b = first_games[k]
        ans.append(f'{a} {b}')
    else:
        pos = (k - num_games - 1) % num_games
        ans.append(f'{champion} {powers_after[pos]}')

print('\n'.join(ans))