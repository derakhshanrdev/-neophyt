try:
    Ex = ValueError()
    Ex.strerror('your number must be between 1 and 10')
    raise Ex
except ValueError as e:
    print('exception ', e.strerror)

    