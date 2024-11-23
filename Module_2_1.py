#Условные операторы if,else,elif
first=int(input('Введите первое число '))
second=int(input('Введите второе число '))
third=int(input('Введите третье число '))
if first == second and second == third:         #Сначала проверка на наименее возможный результат
    print(3)
elif first == second or second == third or first == third:          #Затем менее строгая проверка
    print(2)
else:           #Если ничего не совпало
    print(0)