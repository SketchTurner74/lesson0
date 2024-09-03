immutable_var = (15,True,'Spoon',3.14)
print(immutable_var)
    # immutable_var[0] = 8
    # immutable_var[1] = False
    # immutable_var[2] = 'Fork'
    # immutable_var[3] = 3.41
    # Операции над такими типами данных недопустимы и при выполнении появится ошибка,
    # т.к. кортеж - неизменяемый список.
mutable_list = ['Рододендрон', 10, 15.6, False]
print(mutable_list)
mutable_list[0] = 'Мухоловка'
mutable_list.append(True)
mutable_list.extend('Трио')
mutable_list.remove(15.6)
print(mutable_list)