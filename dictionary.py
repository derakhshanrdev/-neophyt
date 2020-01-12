dic = {'sam': 'red', 'ali': 'blue', 'reza': 'purple'}
print(dic['sam'])
print(dic.items())
print(dic.keys())
for items in dic:
    print(items)
for items in dic:
    print('{name} likes the color {color}'.format(name = items, color = dic[items]))
    