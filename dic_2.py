color = {'0' : 'blue',
         '1' : 'red',  
         '2' : 'black',
         '3' : 'pink'} 
                       

selection = '0'
while True:
    print('0 . blue')
    print('1 . red')
    print('2 . yellow')
    print('3 . black')
    print('4 . quit')
    try:
        selection = str(input('type a number between 0 and 4: '))
    except: #Exception
        print('You must type a number !')
    if selection == '4':
        break
    else:
        for item in selection:
            print('You choosed : ',color[item])
