my_dict = {'Sam':2000, 'Paul':1998, 'Dana':2002}
print('Словарь:',my_dict)
print('Существующее значение:', my_dict['Sam'],'  ', 'Несуществующее значение:', my_dict.get('Nicole', 'Такого значения нет'))
my_dict.update({'John':2001, 'Chris':1987})
a=my_dict.pop('Dana')
print('Удаленное значение:',a)
print('Измененный словарь:',my_dict)
print('_________________________________________________________')
my_set = {1,3.14,3.14,False,1,'Питер',3.14,"Питер"}
print('Множество:', my_set)
my_set.add('Москва')
my_set.add((2,3,4,5))
my_set.discard(3.14)
print('Изменённое множество:', my_set)