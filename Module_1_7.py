#Задача повышенной сложности по 1-му модулю.
grades=[[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students={'Johnny','Bilbo','Steve','Khendrik','Aaron'}
#Ищем среднее арифметическое всех оценок ученика:
First=sum(grades[0])/len(grades[0])
Second=sum(grades[1])/len(grades[1])
Third=sum(grades[2])/len(grades[2])
Fourth=sum(grades[3])/len(grades[3])
Fifth=sum(grades[4])/len(grades[4])
students=list(students)         #Преобразуем множество в список
students.sort()                 #Сортировка по алфавиту
Journal={students[0]:First,students[1]:Second, students[2]:Third,students[3]:Fourth,students[4]:Fifth}
print(Journal)