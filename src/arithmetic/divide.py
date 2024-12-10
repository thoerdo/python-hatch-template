def divide(x, y):

    z = 0

    try:
        z = x / y
        return z
    except ZeroDivisionError as error:
        print(error)
        return 0
