try:
    value = int(input('type a number : '))
    value_2 = int(input('type a number : '))
    output = value / value_2
except ValueError:
    print('you must type a number !')
except ZeroDivisionError:
    print('attempted to divide by zero !')
#except ArithmeticError:
  #  print('undefinded math error ')
else:
    print(output)