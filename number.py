value = int(input('Enter a number\n: '))

if type(value) is int:
    print(str(value) + ' * ' + str(value) + ' = ' + str(value * value))
else: print(str(value) + "is not a number!!!")