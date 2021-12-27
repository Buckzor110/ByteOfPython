try:
    text = input('Введите что-нибудь --> ')
except EOFError:
    print('Ну зачем вы мне сделали EOF?')
except KeyboardInterrupt:
    print('Вы отменили операцию.')
else:
    print('Вы ввели {}'.format(text))