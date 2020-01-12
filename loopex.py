tryagain = True
while tryagain:
    try:
        value = int(input('type a whole number :'))
    except ValueError:
        print('you must type a whole number !')
        try:
            D = input('Do you want to continue?')
        except:
            print('ok, see you next time !')
            tryagain=False
        else:
            if D == 'N':
                tryagain = False
    except KeyboardInterrupt:

        print("You pressed Ctrl+C!")
        print("See you next time!") 
        TryAgain = False
    else:
        print(value) 
        tryagain = False
    
