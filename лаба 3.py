#С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х равных по размерам
#подматриц, B,C,D,E заполняется случайным образом целыми числами в интервале [-10,10].
#Для тестирования использовать не случайное заполнение, а целенаправленное.

#Вариант 3
#Формируется матрица F следующим образом: если в С количество положительных элементов в четных столбцах в области 2 больше,
#чем количество отрицательных  элементов в нечетных столбцах в области 4, то поменять в С симметрично области 1 и 3 местами, иначе С и Е поменять местами несимметрично.
#При этом матрица А не меняется. После чего вычисляется выражение: (F+A)*AT – K * F.
#Выводятся по мере формирования А, F и все матричные операции последовательно.

#B  C               2
#D  E           1       3
#                   4



import random

def matrix(matr):
    for row in matr:
        for elem in row:
            print('{:4}'.format(elem), end='')
        print()


try:
    k = int(input('Введите коэффициент умножения (целое число): '))
    n = int(input('Введите порядок матрицы (целое число, которое больше 4-ёх): '))
    while n<5:
        n = int(input("Вы ввели число не подходящее условию, введите порядок матрицы повторно: "))
    ndl = n // 2
    ndll = ndl
    if n % 2 != 0:
        ndll += 1
    matrA = [[random.randint(-10, 10) for i in range(n)] for j in range(n)]
    print('\nМатрица А')
    matrix(matrA)

    matrcopy = [[elem for elem in raw] for raw in matrA]

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

    matrF = [[elem for elem in raw] for raw in matrA]

    pluscounter = 0
    minuscounter = 0
    for i in range(ndll):
        for j in range(ndll):
            if (j >= i) and (j + i + 1 <= ndll) and (j % 2 != 0) and (j != 0):
                if matrC[i][j] > 0:
                    pluscounter += 1
    print('\n', pluscounter, '- количество положительных чисел в чётных столбцах области 2 подматрицы C')

    for i in range(ndll):
        for j in range(ndll):
            if (i >= j) and (j + i + 1 >= ndll) and ((j % 2 == 0) or (j == 0)):
                if matrC[i][j] < 0:
                    minuscounter += 1
    print('\n', minuscounter, '- количество отрицательных чисел в нечётных столбцах области 4 подматрицы C')

    matrCcopy = [[elem for elem in raw] for raw in matrC]

    if pluscounter > minuscounter:
        print('\n Количество положительных чисел в чётных столбцах области 2 подматрицы C больше, чем количество отрицательных чисел в нечётных столбцах области 4 подматрицы C ')
        print('Меняем местами области 1 и 3 симметрично\n')
        for i in range(ndll):
            for j in range(ndll):
                if (i >= j) and ((i + j + 1) <= ndll):
                    matrC[i][j] = matrCcopy[i][ndll - j - 1]
                    matrC[i][ndll - j - 1] = matrCcopy[i][j]
        for i in range(ndll):
            for j in range(ndl, n):
                matrF[i][j] = matrC[i][j-ndl]

    else:
        print('\nКоличество отрицательных чисел в нечётных столбцах области 4 подматрицы C больше или равно количеству положительных чисел в чётных столбцах области 2 подматрицы C ')
        print('Меняем местами области C и E несимметрично\n')
        if n % 2 != 0:
            for i in range(ndl+1, n):
                for j in range(ndl, n):
                    matrF[i][j] = matrC[i-ndl-1][j-ndl]
        else:
            for i in range(ndl, n):
                for j in range(ndl, n):
                    matrF[i][j] = matrC[i-ndl][j-ndl]
        for i in range(ndll):
            for j in range(ndl, n):
                matrF[i][j] = matrE[i][j-ndl]

    print('Матрица F, с учётом преобразований \n')
    matrix(matrF)

    print("\n F + A =\n")
    matrFplusA = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            matrFplusA[i][j] = matrA[i][j] + matrF[i][j]
    matrix(matrFplusA)

    print('\n Матрица A транспонированная\n')
    matrAT = [[elem for elem in raw] for raw in matrA]
    for i in range(n):
        for j in range(n):
            matrAT[i][j] = matrA[j][i]
    matrix(matrAT)

    print('\n Произведение матрицы A транспонированной на сумму матриц A и F\n')
    matrFandAT = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            for l in range(n):
                matrFandAT[i][j] += matrFplusA[i][l] * matrAT[l][j]
    matrix(matrFandAT)

    print('\n Произведение матрицы F на множитель k')
    matrkF = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            matrkF[i][j] = k * matrF[i][j]
    matrix(matrkF)

    matrresult = [[0 for i in range(n)] for j in range(n)]
    print('\n Результат работы программы. Финальное решение выражения (F+A)*AT – K * F \n')
    for i in range(n):
        for j in range(n):
            matrresult[i][j] = matrFandAT[i][j] - matrkF[i][j]
    matrix(matrresult)

except ValueError:
    print("Вы ввели символ, не являющийся числом. Перезапустите программу и введите число, соответсвующее условию")
