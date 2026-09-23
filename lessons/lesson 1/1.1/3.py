def is_valid(s):
    stack = []
    i = 0
    n = len(s)

    while i < n:
        if s[i] != '<':
            return False  # Должен быть открывающий тег    
        i += 1

        closing = False
        if i < n and s[i] == '/':
            closing = True  # Началась закрывающая часть
            i += 1

        start = i
        while i < n and 'a' <= s[i] <= 'z':
            i += 1
        if i == start:
            return False  # Тег не может быть пустым
        
        if i >= n or s[i] != '>':
            return False  # После текста не закрывающий тег
        text = s[start:i]
        i += 1

        if closing:
            if not stack or stack[-1] != text:
                return False
            stack.pop()
        else:
            stack.append(text)

    return not stack


xml_string = input()
chars = 'abcdefghijklmnopqrstuvwxyz<>/'

ans = ''
for i in range(len(xml_string)):
    orig = xml_string[i]
    for ch in chars:
        if ch == orig:
            continue
        
        candidate = xml_string[:i] + ch + xml_string[i + 1:]
        if is_valid(candidate):
            ans = candidate
            break
    
    if ans:
        break

print(ans)
