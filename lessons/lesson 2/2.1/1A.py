def two_pointer_queue():
    start = 0
    end = 0
    n = 1000
    queue = [None] * n
    command = ''
    
    while command != 'exit':
        command = input()

        if 'push' in command:

            if end == n:
                if end - start == n:
                    print('error')
                    continue
                else:
                    for i in range(end - start):
                        queue[i] = queue[start + i]
            
                    end = end - start
                    start = 0

            num = int(command[-1])
            queue[end] = num
            end += 1
            print('ok')
        elif command == 'pop':
            if start == end:
                print('error')
            else:
                print(queue[start])
                start += 1
        elif command == 'front':
            if start == end:
                print('error')
            else:
                print(queue[start])
        elif command == 'size':
            print(end - start)
        elif command == 'clear':
            start = 0
            end = 0
            print('ok')
        elif command == 'exit':
            print('bye')


def two_stack_queue():
    front_stack = []
    back_stack = []

    command = ''
    while command != 'exit':
        command = input()

        if not front_stack:
            while back_stack:
                front_stack.append(back_stack.pop())

        if 'push' in command:

            num = int(command[-1])
            back_stack.append(num)
            print('ok')
        elif command == 'pop':
            if not front_stack and not back_stack:
                print('error')
            else:                
                print(front_stack.pop())
        elif command == 'front':
            if not front_stack and not back_stack:
                print('error')
            else:
                print(front_stack[0])
        elif command == 'size':
            print(len(front_stack) + len(back_stack))
        elif command == 'clear':
            front_stack = []
            back_stack = []
            print('ok')
        elif command == 'exit':
            print('bye')

    del front_stack
    del back_stack


two_stack_queue()