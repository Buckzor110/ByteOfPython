def PrintMax(x,y):
    '''Выводит максимальное из двух чисел.

    Оба значения должны быть целыми.'''
    x=int(x)
    y=int(y)
    if x>y:
        print(x, 'наибольшее')
    else:
        print(y, 'наибольшее')
PrintMax(3,5)
print(PrintMax.__doc__) ## Одно и то же
help(PrintMax)          ## Одно и то же
