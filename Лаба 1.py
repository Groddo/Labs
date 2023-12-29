# Написать программу, которая читая символы из бесконечной последовательности (эмулируется конечным файлом, читающимся поблочно),
# распознает, преобразует и выводит на экран числа по определенному правилу.
# Числа распознаются по законам грамматики русского языка. Преобразование делать по возможности через словарь.
# Для упрощения под выводом числа прописью подразумевается последовательный вывод всех цифр числа.
# #Регулярные выражения использовать нельзя.

#Вариант 3. #Вещественные числа. В них менять запятую на точку.

delimiter = ' '
correctList = []
with open("numbers.txt", 'r') as file:
   for row in file:
       list =row.split(delimiter)
       for item in list:
           checkAlphabit = 0
           checkPoints = item.count(',')
           checkPoints+= item.count('.')
           for ch in range(len(item)):
               if not item[ch].isdigit() and item[ch] != '.' and item[ch] != ',' and item[ch] != '-':
                   checkAlphabit +=1
               if item[ch] ==',' or item[ch] == '.':
                   checkLeftNum = 1
                   checkRightNum = 1
                   if ch != 0:
                       if item[ch-1].isdigit() or item[ch-1] == '-':
                           checkLeftNum = 1
                       else : checkLeftNum = 0
                   if ch!= len(item) - 1:
                       if item[ch+1].isdigit():
                           checkRightNum = 1
                       else : checkRightNum = 0
                   if checkLeftNum == checkRightNum == 1 and checkPoints==1 and checkAlphabit==0:

                       str = item.replace(',', '.')
                       correctList.append(str)

for i in correctList:
    print(i)
