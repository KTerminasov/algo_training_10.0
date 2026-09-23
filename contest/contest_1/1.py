n = int(input())
answer = []

for step in range(n):
    s = input()
    res = []
    word = ''
    for i in s:
        if i.isupper() and word != '':
            res.append(word)
            word = i.lower()
        else:
            word += i.lower()

    res.append(word)
    answer.append("_".join(res))

print(*answer, sep='\n')
