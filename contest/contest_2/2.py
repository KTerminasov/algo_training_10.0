s = input()

open = s.count('<')
close = s.count('>')
slashes = s.count('/')
num_of_tags = slashes

if num_of_tags == 0 or open != 2 * num_of_tags or close != 2 * num_of_tags:
    print("Impossible") 
else:
    repeats = {}
    
    for letter in s:
        if letter.islower():
            if letter in repeats:
                repeats[letter] += 1
            else:
                repeats[letter] = 1
    
    possible = True

    for rep in repeats.values():
        if rep % 2 != 0:
            possible = False
    
    if not possible:
        print("Impossible") 
    else:
        
        letters = []
        for letter, rep in repeats.items():
            letters.extend([letter]*(rep // 2))
        
        half = len(letters)
        if half < num_of_tags:
            print("Impossible")
        else:
            names = []
            index = 0

            for i in range(num_of_tags - 1):
                names.append(letters[index])
                index += 1
            names.append(''.join(letters[index:]))
            open_part = ''.join('<' + name + '>' for name in names)
            close_part = ''.join('</' + name + '>' for name in reversed(names))
            print(open_part + close_part)




