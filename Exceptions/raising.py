class ShortInputException(Exception):
    '''Пользовательскй класс исключения.'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

try:
    text = input('Введите что-нибудь --> ')
    if len(text)<3:
        raise ShortInputException(len(text), 3)
    # Здесь может происходить обычная работа
except EOFError:
    print('Ну зачемм вы сделали мне EOF?')
except ShortInputException as ex:
    print('ShortInputException: Длина введенной строки -- {}; \
ожидалось, как минимум, {}'.format(ex.length, ex.atleast))
else:
    print('Не было исключений')