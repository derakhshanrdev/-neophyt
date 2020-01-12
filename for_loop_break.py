word = 'derakhshan'
count = 1
for letter in word:
    print('letter', count, 'is', letter)
    count += 1
    if count == 6:
        print('the character is too long!')
        break