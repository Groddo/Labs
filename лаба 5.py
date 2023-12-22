import time
import matplotlib.pyplot as plt

def Rec(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    else:
        return 5*Rec(n-1)-2*Rec(n-2)

def Iter(n):
    if n == 1:
        return 2
    else:
        fn = [1, 2, 1]
        for i in range(1, n):
            fn[2]= 5*fn[1] - 2*fn[0]
            fn[0], fn[1] = fn[1], fn[2]
        return fn[2]

try:
    x=int(input('Введите натуральное число: '))
    while x < 1:
        print("Вы ввели не натуральное число")
        x = int(input('Введите новое число: '))

    s=int(input('Введите длину шага, на основе которого будет строиться таблица: '))
    while s < 1:
        s=int(input('Вы ввели число не являющееся натуральным, введите новое число: '))

    k = 1
    if x >= 39:
        k = int(input('Вы ввели число, которое больше 38. Вычисление с помощью рекурсивного подхода займёт много времени, вы желаете получить результат с помощью рекурсивного метода? ВВедите "1", если да и "0", если нет: '))
    while k!=0 and k!=1:
        k = int(input("\nВы ввели не 1 и не 0. Введите 1, чтобы продолжить, или 0, чтобы завершить программу:\n"))

    if k != 0:
        t01 = time.time()
        resultREC = Rec(x)
        t1 = time.time()
        print('\n Рекурсия:',resultREC ,'\n Время:', t1-t01)

    t02 = time.time()
    resultIter = 2
    if x > 1:
        resultIter = Iter(x)
    t2 = time.time()
    print('\n Итерация:', resultIter, '\n Время:', t2-t02)

    RecTime = []
    RecRess = []
    IterTime = []
    IterRess = []
    values = list(range(1, x + 1, s))

    for x in values:
        start = time.time()
        RecRess.append(Rec(x))
        end = time.time()
        RecTime.append(end-start)

        start=time.time()
        IterRess.append(Iter(x))
        end=time.time()
        IterTime.append(end-start)

    tablica = []
    chislo = 1
    for a, b in enumerate(values):
        tablica.append([chislo, RecTime[a], IterTime[a], RecRess[a], IterRess[a]])
        chislo += s

    print('{:<7}|{:<22}|{:<22}|{:<22}|{:<22}'.format('Число', 'Время рекурсии (с)', 'Время итерации (с)', 'Значение рекурсии','Значение итерации'))

    for inf in tablica:
        print('{:<7}|{:<22}|{:<22}|{:<22}|{:<22}'.format(inf[0], inf[1], inf[2], inf[3], inf[4]))

    plt.plot(values, RecTime, label='Рекурсия')
    plt.plot(values, IterTime, label='Итерация')
    plt.xlabel('Число')
    plt.ylabel('Время (с)')
    plt.title('Сравнение рекурсивного и итерационного подхода')
    plt.legend()
    plt.show()

    print('Неэффективность рекурсионного решения заметна уже при x>35, дальнейшие вычисления проводятся очень долго, в то время как итерация выполняется за доли секунды и может вычислять значения функции вплоть до x=6524')

except ValueError:
    print("Вы ввели символ не подходящий по условию или слишком большое число, перезапустите программу и введите натуральное число, которое будет меньше 6525")

except RecursionError:
    print("Вы ввели слишком большое число, относительная максимальная глубина рекурсии превышена. Перезапустите программу и введите меньшее число, если хотите получать результат работы реккурсионного подхода. ")