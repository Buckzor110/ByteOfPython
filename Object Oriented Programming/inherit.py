class SchoolMember:
    '''Представляет любого человека в школе'''
    def __init__(self,name,age):  # Инициализируем объекты, которые нам нужны
        self.name = name
        self.age = age
        print('Создан SchoolMember: {0}'.format(self.name))
    def tell(self):
        '''Вывести информацию'''
        print('Имя: {0}, Возраст: {1}'.format(self.name, self.age),end=' ')

class Teacher(SchoolMember):
    '''Пердставляет преподаваетля'''
    def __init__(self, name, age, salary):  # Инициализируем объекты, нахоящиеся в подклассе
        SchoolMember.__init__(self, name, age)  # Большинство объектов берем из надкласса
        self.salary = salary
        print('Создан Teacher: {0}'.format(self.name))
    def tell(self):
        SchoolMember.tell(self)
        print('Зарплата: {0}'.format(self.salary))
class Student(SchoolMember):
    '''Представляет студента'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('Создан Student: {0}'.format(self.name))
    def tell(self):
        SchoolMember.tell(self)
        print('Оценки: {0}'.format(self.marks))
t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)
print()
members = [t, s]
for member in members:
    member.tell()
