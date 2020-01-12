def re(argcount, *varargs):
    print('you passed', argcount, 'arg')
    for arg in varargs:
        print(arg) 

print(re(5, 'a', 'b', 'c', 'd', 'f'))
#a =[a, b, c, d, f]
#print(re(4, a))