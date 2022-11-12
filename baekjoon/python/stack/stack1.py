def push(stack, number):
    stack.append(number)


def pop(stack):
    if len(stack) == 0:
        print('-1')
    else:
        print(stack.pop())


def top(stack):
    if len(stack) == 0:
        print('-1')
    else:
        print(stack[-1])


def empty(stack):
    if len(stack) == 0:
        print('1')
    else:
        print('0')


def main():
    num_command = int(input())
    stack = []

    while num_command != 0:
        command = input()

        if command.find('push') != -1:
            number = int(command.split()[1])

            push(stack, number)

        elif command == 'pop':
            pop(stack)

        elif command == 'size':
            print(len(stack))

        elif command == 'top':
            top(stack)

        elif command == 'empty':
            empty(stack)

        num_command -= 1

if __name__ == "__main__":
    main()
