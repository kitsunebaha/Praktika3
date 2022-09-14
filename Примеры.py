
fio={'firstName':'Бахытжан','secondName':'Сабитович','lastName':'Нургалиев'}

# Доступ к значению
print("Полное имя/фамилия: " + fio['firstName'] + fio['lastName'])  

# Перебор всех пар ключ-значение
fio={'firstName':'Анна','secondName':'Алексеева','lastName':'Логашина','date':'2022-09-10','period':14}
for name,s in fio.items():
    print(name + ':' + str(s) )

# преобразую представление в список, списокявляется последовательностью кортежей (ключ, значение) - то, что получает dict для создания словаря
print(list(fio.items()))

# функция sorted возвращает новый отсортированный список 
for name in sorted(fio.items()):
    print(name)

# противоположный порядок вывода
for name in sorted(fio.keys(), reverse=True):
    print(name)

for name in sorted(fio.items(),reverse=True):
    print(name)

# Перебираем все ключи
fio={'firstName':'Анна','secondName':'Алексеева','lastName':'Логашина','date':'2022-09-10','period':14}
for name in fio.keys():
    print(name + '')

# Перебор всех значений
# Результат вызова .values также является представлением. Он отражает
# # # текущее состояние значений, находящихся в словаре
for number in fio.values():
    print(str(number) + ' ' + 'статус:по совместительству')

# Для вставки значений в словарь используют индексные операции:
fio['occupation'] = 'programming'

# поиск индексной операцией:
print(fio['occupation'])

# Метод .get словаря получает значение, соответствующее ключу
staff = fio.get('Должность', 'преподаватель')
print(staff)

# операции подсчета
import collections
count = collections.Counter(['Чернова', 'Семенов', 'Ветров', 'Чернова'])
print(count)

# только Чернова
print(count['Чернова'])

# Задание: Связать фамилию участника с двумя группами
surnamesGroup = ['Чернова', 'Семенов', 'Ветров', 'Мостовой']
candidate = ['Чернова']
surnames = {}
for name in surnamesGroup:
    surnames.setdefault(name, []).append('DKMO-21')
for name in candidate:
    surnames.setdefault(name,[]).append('DKMO-22')
    print(surnames['Чернова'])

# Python не позволяет добавлять и удалять данные из словаря во время егоперебора.
# В таких ситуациях Python выдает исключение RuntimeError:
data = {'surname':'Чернова', 'surname':'Семенов','surname': 'Ветров', 'surname':'Мостовой'}
for key in dict(data):
    del data[key]