try:
    value= int(input('type a number : '))
except:
    print('you must type a number !')
try:
    value_2 = int(input('type a number : '))
except:
    print('you must type a number !')
try:
    operator = input('type an operator : ')
except :
    print('you must type an operator !')


def cal(value, value_2, operator='+' ):
        if value and value_2 == 0:
            print ('the nember is zero!')
        else:
            if operator == '+':
                return value + value_2 
            elif operator == '-':
                return value - value_2
            elif operator == '*':
                return value * value_2 
            elif operator == '/':
                return value / value_2 


print(cal(value, value_2, operator))