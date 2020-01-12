my_stack = []
size_stack = 3
def di():
    print( 'stack currently contains :')
    for i in my_stack:
        print(i)

def push(value):
    if my_stack < size_stack:
        my_stack.append(value)
    else:
        print( 'stack is full !')


def pop():
    if len(my_stack) > 0:
        my_stack.pop()
    else:
        print( 'stack is empty! ')
push(1)
push(2)
push(3)
di()
input('press any key when ready ')
push(4)
di()
input('press any key when ready ')
pop()
di()
input('press any key when ready ')
pop()
pop()
pop()
di()




































