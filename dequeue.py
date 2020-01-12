import collections
mydeque = collections.deque('abcdef', 10)
print(mydeque)
print('starting state : ')
for item in mydeque:
    print(item, end = " ")
