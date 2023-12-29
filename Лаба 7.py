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


import itertools


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


listArray = []
listArray.append(Fruit('яблоко','красный',False))
listArray.append(Fruit('банан','жёлтый',False))
listArray.append(Fruit('мандарин','оранжевый',True))
listArray.append(Fruit('слива','фиолетовый',False))
listArray.append(Fruit('груша','зелёный',False))
listArray.append(Fruit('личи','коричневый',True))
listArray.append(Fruit('питахайя','белый',False))
listArray.append(Fruit('чомпу','розовый',False))
listArray.append(Fruit('мангостин','чёрный',False))
listArray.append(Fruit('гранат','бордовый',False))

childAllergic = ''
print('Есть ли у ребёнка аллергия на какие-либо фрукты из списка: банан, слива, мандарин, яблоко, груша, личи, питахайя, чомпу, мангостин, гранат?')
while childAllergic not in ['да','нет']:
    childAllergic = input('Введите "да" или "нет": ')

colorcheck = input('Есть ли у ребёнка нелюбимый цвет?\nВведите цвет, который не любит ребёнок или введите "нет", если такого цвета нет,'
                    '\nесли введённый вами текст не будет являться цветом или фрукта такого цвета нет в меню,'
                    ' то тогда ваш ответ будет равносилен вводу "нет": ')

firstcheckedlist = Fruit.checkFruitForAllergic(listArray) if childAllergic == 'да' else listArray

secondcheckedlist = firstcheckedlist if colorcheck == 'нет' else Fruit.checkFruitForColor(firstcheckedlist, colorcheck)


menu = list(itertools.permutations(secondcheckedlist, 7))
for i, variant in enumerate(menu, 1):
    print(f'Меню №{i}:{[fruit.name for fruit in variant]}')
