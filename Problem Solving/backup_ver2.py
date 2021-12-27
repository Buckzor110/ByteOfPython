import os
import time
# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
source = ['"C:\\My Documents"', 'C:\\Code']
# Заметьте, что для имён, содержащих пробелы, необходимо использовать
# двойные кавычки внутри строки.
# 2. Резервные копии должны храниться в основном каталоге резерва.
target_dir = 'E:\\Backup\\2' # Подставьте ваш путь.
# 3. Файлы помещаются в zip-архив.
# 4. Текущая дата служит именем подкаталога в основном каталоге
today = target_dir + os.sep + time.strftime('%d%m%Y')
# Текущее время служит именем zip-архива
now = time.strftime('%S%M%H')
# Создаём каталог, если его ещё нет
if not os.path.exists('E:\\Backup\\2'):
    os.mkdir('E:\\Backup\\2')
if not os.path.exists(today):
    os.mkdir(today)
    print('Каталог успешно создан', today)
# Имя zip-файла
target = today + os.sep + now + '.zip'

# 5. Используем команду "zip" для помещения файлов в zip-архив
zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))
# Запускаем создание резервной копии
if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')