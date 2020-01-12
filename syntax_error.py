try:
    s = input('type a letter : ')
except Exception:
    print('type a string')
except SyntaxError:
    print('you failed !')
except NameError:
    print('type a stringgg ')
