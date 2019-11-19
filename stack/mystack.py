from stack.gugudan import dan

size = 0
stack_list = []
stack_size = 5
# top = -1


def push(item):
    global size
    global stack_list
    if size == 5:
        print('stack is {}'.format('over flow'))
        return
    size = size + 1
    stack_list.insert(size, item)


def push_native(stack, top, item):
    if top == 4:
        print('stack is {}'.format('over flow'))
        return top
    stack.append(item)
    top = top + 1
    return int(top)


def pop():
    global stack_list
    global size
    if size == 0:
        print('stack is {}'.format('under flow'))
        return
    size = size - 1
    return stack_list.pop()


def pop_native(stack, top):
    if top == 0:
        print('stack is {}'.format('under flow'))
        return None, top
    top = top - 1
    return stack.pop(), int(top)


def stack_prn():
    global stack_list
    # print(list[0:len(list)])
    if size > 0:
        for item in stack_list[0:len(stack_list)-1]:
            print('{}->'.format(item), end='')
        print(stack_list[len(stack_list)-1])


def stack_native_prn(stack, top):
    for item in stack[0:len(stack)-1]:
        print('{}->'.format(item), end='')
    print(stack[len(stack)-1])


if __name__ == "__main__":
    stack = []
    top = -1
    for item in ['a', 'b', 'c', 'd', 'e', 'f']:
        # push(item)
        top = push_native(stack, top, item)
        stack_native_prn(stack, top)

    for cnt in range(0, 5):
        item, top = pop_native(stack, top)
        print(item, top)
        stack_native_prn(stack, top)

    # dan(3)
