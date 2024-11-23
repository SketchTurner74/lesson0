#Задача повышенной сложности по 1-му модулю.
grades=[[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students={'Johnny','Bilbo','Steve','Khendrik','Aaron'}
First=sum(grades[0])/len(grades[0])      #Ищем среднее арифметическое оценок первого ученика
Second=sum(grades[1])/len(grades[1])     #Ищем среднее арифметическое оценок второго ученика
Third=sum(grades[2])/len(grades[2])      #Ищем среднее арифметическое оценок третьего ученика
Fourth=sum(grades[3])/len(grades[3])     #Ищем среднее арифметическое оценок четвертого ученика
Fifth=sum(grades[4])/len(grades[4])      #Ищем среднее арифметическое оценок пятого ученика
students=list(students)         #Преобразуем множество в список
students.sort()                 #Сортировка по алфавиту
Journal={students[0]:First,students[1]:Second, students[2]:Third,students[3]:Fourth,students[4]:Fifth}      #Формируем итоговый словарь
print(Journal)
