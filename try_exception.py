try: 
    value = int(input('type a number between 1 and 10 :  '))
except ValueError :#<--- تیکه اخرو نزاری جالب میشه 
    print('you must type a number between 1 and 10 ! ')
else:
    if value > 1 and value <= 10 :
        print('you type ', value)
    else:
        print('your number is invalid !')        
