end_buff, buff, comma = [], [], ',' #Конечный буффер подходящих, изменённых чисел; Рабочий буффер; Переменная для проверки условия
with open('Numbers.txt') as f:
    while True:
        a = f.read(1)
        if a!=' ' and a!='' and a!='\n'  and a!='.': #Отделяем числа друг от друга
            buff.append(a)   #И добавляем подходящие в рабочий буффер
        else:
            if comma in buff: #Проверяем вещественное ли число в рабочем буффере
                for i in buff: #Заменяем запятую на точку
                    if i == ',':
                        i = '.'
                    end_buff.append(i)#Заполняем конечный буффер
                end_buff.append(' ')#Добавляем пробелы между числами
            buff.clear()
        if a == '':
            break
    end_buff[-1]='' #Избавляемся от лишнего пробела в конце
print(''.join(end_buff))