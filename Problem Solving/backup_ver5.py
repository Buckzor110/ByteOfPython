import os
import time
import zipfile
# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
source = ['C:\\Code', 'C:\\My Documents']
# Заметьте, что для имён, содержащих пробелы, необходимо использовать
# двойные кавычки внутри строки.
# 2. Резервные копии должны храниться в основном каталоге резерва.
target_dir = 'E:\\Backup\\5'  # Подставьте ваш путь.
# 3. Файлы помещаются в zip-архив.
# 4. Текущая дата служит именем подкаталога в основном каталоге
today = target_dir + os.sep + time.strftime('%Y%m%d')
# Текущее время служит именем zip-архива
now = time.strftime('%H%M%S')
# Запрашиваем комментарий пользователя для имени файла
comment = input('Введите комментарий --> ')
if len(comment) == 0:  # проверяем, введён ли комментарий
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
             comment.replace(' ', '_') + '.zip'
# Создаём каталог, если его ещё нет
if not os.path.exists('E:\\Backup\\5'):
    os.mkdir('E:\\Backup\\5')
if not os.path.exists(today):
    os.mkdir(today)  # создание каталога
    print('Каталог успешно создан', today)
# Создаю пустой архив
myzip = zipfile.ZipFile(target, 'w')
# Добавляю в архив файлы, которые необходимо заархивировать
for a in source:
    for folder, subfolders, files in os.walk(a):
        for file in files:
            myzip.write(os.path.join(folder, file))


