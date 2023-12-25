#С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N),
#состоящая из 4-х равных по размерам подматриц, B,C,D,E заполняется случайным образом целыми числами в интервале [-10,10].
#Для отладки использовать не случайное заполнение, а целенаправленное. Вид матрицы А:     B        C
#                                                                                         D        E
#Для простоты все индексы в подматрицах относительные. 
#По сформированной матрице F (или ее частям) необходимо вывести не менее 3 разных графиков.
#Программа должна использовать функции библиотек numpy  и mathplotlib
#
#Вариант 3.   
#Формируется матрица F следующим образом: скопировать в нее А и если в С количество положительных элементов в четных столбцах больше,
#чем количество отрицательных  элементов в нечетных столбцах, то поменять местами В и С симметрично, иначе С и Е поменять местами несимметрично.
#При этом матрица А не меняется. После чего если определитель матрицы А больше суммы диагональных элементов матрицы F,
#то вычисляется выражение: A*AT – K * F-1, иначе вычисляется выражение (A-1 +G-F-1)*K, где G-нижняя треугольная матрица, полученная из А. 





import numpy as np
from matplotlib import pyplot as plt
import random


def matrix(matr):
    for row in matr:
        for elem in row:
            print('{:4}'.format(elem), end='')
        print()

    np.set_printoptions(linewidth=1000)
try:
    k = int(input('Введите коэффициент умножения (целое число): '))
    n = int(input('Введите порядок матрицы (целое число, которое больше 2-ух): '))
    while n<3:
        n = int(input("Вы ввели число не подходящее условию, введите порядок матрицы повторно: "))
    ndl = n // 2
    ndll = ndl
    if n % 2 != 0:
        ndll += 1
    matrA = np.random.randint(-10.0, 11.0, (n, n))
    print('\nМатрица А')
    matrix(matrA)

    matrcopy = matrA.copy()

    print('\nПодматрица B')
    matrB = [[0 for i in range(ndll)] for j in range(ndll)]
    for i in range(ndll):
        for j in range(ndll):
            matrB[i][j] = matrcopy[i][j]
    matrix(matrB)

    print('\nПодматрица С')
    matrC = [[0 for i in range(ndll)] for j in range(ndll)]
    for i in range(ndll):
        for j in range(ndl, n):
            matrC[i][j - (ndl)] = matrcopy[i][j]
    matrix(matrC)

    print('\nПодматрица D')
    matrD = [[0 for i in range(ndll)] for j in range(ndll)]
    for i in range(ndl, n):
        for j in range(ndll):
            matrD[i-(ndl)][j] = matrcopy[i][j]
    matrix(matrD)

    print('\nПодматрица E')
    matrE = [[0 for i in range(ndll)] for j in range(ndll)]
    for i in range(ndl, n):
        for j in range(ndl, n):
            matrE[i - (ndl)][j - (ndl)] = matrcopy[i][j]
    matrix(matrE)

    matrF = matrA.copy() #[[elem for elem in raw] for raw in matrA]

    pluscounter = 0
    minuscounter = 0
    for i in range(ndll):
        for j in range(ndll):
            if (j % 2 != 0) and (j != 0):
                if matrC[i][j] > 0:
                    pluscounter += 1
    print('\n', pluscounter, '- количество положительных чисел в чётных столбцах подматрицы C')

    for i in range(ndll):
        for j in range(ndll):
            if (j % 2 == 0) or (j == 0):
                if matrC[i][j] < 0:
                    minuscounter += 1
    print('\n', minuscounter, '- количество отрицательных чисел в нечётных столбцах подматрицы C')

    matrCcopy = matrC.copy()
    matrBcopy = matrB.copy()

    if pluscounter > minuscounter:
        print('\n Количество положительных чисел в чётных столбцах подматрицы C больше, чем количество отрицательных чисел в нечётных столбцах')
        print('Меняем местами подматрицы B и C симметрично\n')
        for i in range(ndll):
            for j in range(ndll):
                matrB[i][j] = matrCcopy[i][ndll - j - 1]
                matrC[i][ndll - j - 1] = matrBcopy[i][j]
        for i in range(ndll):
            for j in range(ndll):
                matrF[i][j] = matrB[i][j]
        if n%2 == 0:
            for i in range(ndll):
                for j in range(ndll, n):
                    matrF[i][j] = matrC[i][abs(ndll - j)]
        else:
            for i in range(ndll):
                for j in range(ndll, n):
                    matrF[i][j] = matrC[i][j - ndll + 1]
    else:
        print('\nКоличество отрицательных чисел в нечётных столбцах подматрицы C больше или равно количеству положительных чисел в чётных столбцах')
        print('Меняем местами подматрицы C и E несимметрично\n')
        if n % 2 != 0:
            for i in range(ndl + 1, n):
                for j in range(ndl, n):
                    matrF[i][j] = matrC[i - ndl - 1][j - ndl]
        else:
            for i in range(ndl, n):
                for j in range(ndl, n):
                    matrF[i][j] = matrC[i - ndl][j - ndl]
        for i in range(ndll):
            for j in range(ndl, n):
                matrF[i][j] = matrE[i][j - ndl]

    print('Матрица F, с учётом преобразования \n')
    matrix(matrF)

    try:
        detA = np.linalg.det(matrcopy)
        print('\nОпределитель матрицы A =', detA, '\n')
        if detA > sum(np.diagonal(matrF)):
            print(
                f'Определитель матрицы А = {detA}, он больше суммы диагональных элементов матрицы F = {sum(np.diagonal(matrF))},'
                f' поэтому считаем выражение A*AT – K * F^-1 = \n {matrA * matrA.transpose() - k * np.linalg.inv(matrF)}')
        else:
            trG = np.tri(n) * matrA
            print(
                f'Определитель матрицы А = {detA}, он меньше или равен сумме диагональных элементов матрицы F = {sum(np.diagonal(matrF))},'
                f' поэтому считаем выражение (A^-1 +G-F^-1)*K = \n {(np.linalg.inv(matrA) + trG - np.linalg.inv(matrF)) * k}')

    except np.linalg.LinAlgError:
        print("Одна из матриц является вырожденной (определитель равен 0), поэтому обратную матрицу найти невозможно.")

    print('\nГрафики будут строиться на основе матрицы F = \n', matrF, '\n')

    matrFT = matrF.transpose()
    plt.subplot(111)
    plt.axis([0, (n-1), -10, 10])
    plt.title('Обычный график точек')
    plt.xlabel('Номер элемента в строке', color='red')
    plt.ylabel('Значение элемента', color='blue')
    plt.plot(matrFT)
    plt.show()

    plt.subplot(111)
    plt.imshow(matrF, cmap='viridis')
    plt.title('Тепловая карта')
    plt.xlabel('Столбцы', color='red')
    plt.ylabel('Строки', color='blue')
    plt.colorbar()
    plt.show()

    values = []
    valuemax = 0
    valuemin = 0
    for i in matrF:
        values.append(sum(i)/len(i))
    index = np.arange(n)
    valuemax = max(index)
    valuemin = min(index)

    plt.subplot(111)
    plt.axis([0, (n - 1), (min(values)-1), (max(values)+1)])
    plt.title('Столбчатая диаграмма. Среднее значение элемента в каждой строке')
    plt.bar(index, values)
    plt.show()

except ValueError:
    print("Вы ввели символ, не являющийся числом. Перезапустите программу и введите число, соответсвующее условию")
