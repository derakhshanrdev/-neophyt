try: 
    Value = int(input('type a number between 1 and 10 :  '))
except ValueError:
    print('you must type a number between 1 and 10 ! ')
except KeyboardInterrupt:
    print('you pressed ctrl + c')
else:
    if Value > 1 and Value <= 10 :
        print('you type ', Value)
    else:
        print('your number is invalid !')        
