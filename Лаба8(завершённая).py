# Задание на л.р. №6
# Задание состоит из двух частей.
# 1 часть – написать программу в соответствии со своим вариантом задания.
# 2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение
# на характеристики объектов и целевую функцию для оптимизации решения.
# У няни 10 разных фруктов (ф1,…ф10).
# Сформировать (вывести) все возможные варианты меню полдника (1 фрукт) для ребенка на неделю.
# Усложнение 1: у ребёнка может быть аллегрия, а может и не быть
# Усложнение 2: у ребёнка есть нелюбимый цвет, фрукт с таким цветом он есть не будет

# задание на лабораторную работу №7.
# Требуется для своего варианта второй части л.р. №6 (усложненной программы) написать объектно-ориентированную реализацию.
# В программе должны быть реализованы минимум один класс, три атрибута, два метода

#Требуется для своего варианта второй части л.р. №6 (усложненной программы) или ее объектно-ориентированной реализации (л.р. №7) разработать реализацию
# с использованием графического интерфейса.
# Допускается использовать любую графическую библиотеку питона.  Рекомендуется использовать внутреннюю библиотеку питона  tkinter.
#В программе должны быть реализованы минимум одно окно ввода, одно окно вывода, текстовое поле, кнопка.


import itertools
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText as st

#Класс Fruit из 7-ой лабараторной работы
class Fruit:
    name = str
    color = str
    allergicFlag = bool
    def __init__(self, name, color, allergicFlag):
        self.name = name
        self.color = color
        self.allergicFlag = allergicFlag

    def checkFruitForColor(fruitList=list, redFlagToFruit=str):
        goodItemList = []
        for item in fruitList:
            if item.color != redFlagToFruit:
                goodItemList.append(item)
        return goodItemList

    def checkFruitForAllergic(fruitList=list):
        goodItemList = []
        for item in fruitList:
            if item.allergicFlag != True:
                goodItemList.append(item)
        return goodItemList

#Список всех фруктов
listArray = []
listArray.append(Fruit('яблоко','красный',False))
listArray.append(Fruit('банан','жёлтый',False))
listArray.append(Fruit('мандарин','оранжевый',True))
listArray.append(Fruit('слива','фиолетовый',False))
listArray.append(Fruit('груша','зелёный',False))
listArray.append(Fruit('личи','коричневый',False))
listArray.append(Fruit('питахайя','белый',False))
listArray.append(Fruit('чомпу','розовый',False))
listArray.append(Fruit('мангостин','чёрный',False))
listArray.append(Fruit('гранат','бордовый',False))
childAllergic = ''
secondcheckedlist = []
input_color = 'нет'

#Закрывает 1-ое окно
def click_button():
    okno.destroy()

#Функция 2-ой кнопки, отвечающая за подсчёты и создание окна вывода
def schet(childAllergic = str, colorcheck = str):
    k=0
    firstcheckedlist = Fruit.checkFruitForAllergic(listArray) if childAllergic == 'да' else listArray
    secondcheckedlist = firstcheckedlist if colorcheck == 'нет' else Fruit.checkFruitForColor(firstcheckedlist,colorcheck)
    menu = list(itertools.permutations(secondcheckedlist, 7))
    for i in menu:
        k+=1

    canvas2.create_rectangle(50, 215, 590, 245, fill='#fff0f5', outline='#7200a3')
    canvas2.create_text(320, 230, text=f'Итого получилось {k} различных списков меню', font='Arial 12')

    vivod = Tk()

    vivod.title('Все варианты меню')
    vivod.geometry('480x320')
    vivod.resizable(False, False)

    text = st(vivod, bg='#fff0f5', wrap='none')
    for x in menu:
        listoffruits = ''
        for fruit in x:
            listoffruits += f'{fruit.name} '

        listoffruits += '\n'
        text.insert('1.0', listoffruits)


    text.pack(anchor='nw', fill=BOTH, expand=True)
    text.config(state=DISABLED)

    vivod.mainloop()

#Первое окно, содержащее в себе информацию и принимающее входные данные
okno = Tk()

okno['bg'] = '#7200a3'
okno.title('Программа для подсчёта количества всех возможных комбинаций полдников для одной недели')
okno.geometry('1000x800')

canvas = Canvas(okno, bg='#ba66ff', height=700, width=640)
canvas.pack(anchor=N)

canvas.create_rectangle(30,160,610,290, fill='#fff0f5', outline='#7200a3')
canvas.create_text(320,45, font='Arial 11', text='Ниже представлена таблица в которой указаны все фрукты, которые')
canvas.create_text(320,70, font='Arial 11', text='могут быть поданы на полдник детям.')
canvas.create_text(320,130, font='Arial 11', text='Цвет шрифта, которым написано название фрукта,соответствует цвету фрукта.')
canvas.create_line(30,225,610,225, fill='#7200a3')
canvas.create_line(146,160,146,290, fill='#7200a3')
canvas.create_line(262,160,262,290, fill='#7200a3')
canvas.create_line(378,160,378,290, fill='#7200a3')
canvas.create_line(494,160,494,290, fill='#7200a3')
canvas.create_text(89,192.5, text='Яблоко', font='Georgia 14', fill='red')
canvas.create_text(204,192.5, text='Банан', font='Georgia 14', fill='#fde910')
canvas.create_text(320,192.5, text='Мандарин', font='Georgia 14', fill='#ffa500')
canvas.create_text(436,192.5, text='Слива', font='Georgia 14', fill='#7200a3')
canvas.create_text(552,192.5, text='Груша', font='Georgia 14', fill='#008000')
canvas.create_text(89,257.5, text='Личи', font='Georgia 14', fill='#5e2916')
canvas.create_text(204,257.5, text='Питахайя\n  (белый)', font='Georgia 14', fill='#000000')
canvas.create_text(320,257.5, text='Чомпу', font='Georgia 14', fill='#ff8fa2')
canvas.create_text(436,257.5, text='Мангостин', font='Georgia 14', fill='#000000')
canvas.create_text(552,257.5, text='Гранат', font='Georgia 14', fill='#9b2d30')

canvas.create_text(320,355, text='Есть ли у ребёнка нелюбимый цвет? Фрукт с таким цветом будет убран из меню.', font='Arial 10')
canvas.create_text(320,385, text='Введите название цвета строчными буквами если есть. Любой другой ввод будет равносилен "нет".', font='Arial 10')

#Строка принимающая текст
color = StringVar()
entry = Entry(canvas, textvariable=color)
entry['bg'] = '#fff0f5'
canvas.create_window(320,445, window=entry, height='50', width='600')

# 2 кнопки, включение одной из них означает отключение другой
canvas.create_text(310, 500, text='Есть ли у ребёнка аллергия на цитрусовые?', anchor=E, font='Arial 10')
lang = StringVar(value='нет')
yes_btn = ttk.Radiobutton(canvas, text='да  ', value='да', variable=lang)
no_btn = ttk.Radiobutton(canvas, text='нет', value='нет', variable=lang)
yes_btn.place(x=50, y=520)
no_btn.place(x=50, y=550)

close_btn = ttk.Button(text='Подтвердить ввод', command=click_button)
canvas.create_window(320,630, window=close_btn, height='50', width='150')
okno.mainloop()

#Создание 2-го окна
root = Tk()
root.title('Результат работы программы')
root.geometry('640x750')
canvas2 = Canvas(root, bg='#ba66ff', height=750, width=640,)
canvas2.pack(anchor=N)

#Главная кнопка в программе, отвечающая за подсчёт и вывод
schets = ttk.Button(text='получить результат', command=lambda: schet(lang.get(), color.get()))
canvas2.create_window(320,170, window=schets, height='50', width='200')
canvas2.create_text(320,70, text='Подсчёт может занять 15-20 секунд после нажатия кнопки', font='Arial 13')
canvas2.create_text(320,95, text='Пожалуйста, подождите', font='Arial 13')

root.mainloop()

