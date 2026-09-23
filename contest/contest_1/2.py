s = input()
t = input()

count_app = [0] * 26
max_app = [0] * 26
for letter in t:
    max_app[ord(letter) - ord('a')] += 1

res = 0
left = 0
for right, letter in enumerate(s):
    ind = ord(letter) - ord('a')
    count_app[ind] += 1

    while count_app[ind] > max_app[ind]:
        left_ind = ord(s[left]) - ord('a')
        count_app[left_ind] -= 1
        left += 1
    
    res += right - left + 1

print(res)
