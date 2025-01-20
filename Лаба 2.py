# Лабораторная работа №2 #Написать программу, которая читая файл, распознает, преобразует и выводит на экран числа по определенному правилу.
# Числа распознаются по законам грамматики русского языка.
# Преобразование делать по возможности через словарь.
# Для упрощения под выводом числа прописью подразумевается последовательный вывод всех цифр числа.
# Распознование делать через регулярные выражения. В вариантах, где есть параметр К, К заменяется на любое число.

#Вариант 3. #Вещественные числа. В них менять запятую на точку.


import re


delimiter = ' '
correctList = []
with open("Numbers.txt", 'r') as file:
   for row in file:
       list = row.split(delimiter)
       for item in list:
           item = item.replace(',', '.')
           counter = item.count('.')
           if counter == 1:
               buffalf = re.search(r'[а-яА-яеЁa-zA-Z?&*%;$#№@"!`~_=/|]', item)
               if buffalf == None:
                   buff1 = re.findall(r"[+-]?[0-9]*[.,][0-9]+", item)
                   if buff1 != []:
                       correctList.append(buff1)
                   buff2 = re.findall(r"[+-]?[0-9]+[.,][0-9]*", item)
                   if buff2 != buff1 and buff2 != []:
                       correctList.append(buff2)
print(correctList)
