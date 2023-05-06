# F(1) = G(1) = 1; F(n) = – 3*G(n–1), G(n) = F(n–1) , при n >=2


import time
from matplotlib import pyplot
try:
    n = int(input("Введите число n больше или равно 2: "))
    while n<2:
        n=int(input("Введите число n больше или равно 2:"))


    def G(n):
        if n <= 1:
            return 1
        else:
            return F(n - 1)


    def F(n):
        if n <= 1:
            return 1
        else:
            return -3 * G(n)


    def Iteratively(n):
        if n == 1:
            return 1
        else:
            res = 1
            for i in range(2, n + 1):
                res = res * -3
            return res


    startr = time.time()
    if n == 1:
        rec = 1
    else:
        rec = F(n)
    endr = time.time()
    timer = endr - startr
    print("Рекурсивно при n = {} F(n) = {}, решено за {:.2f} секунд)".format(n, rec, timer))

    starti = time.time()
    ite = Iteratively(n)
    endi = time.time()
    timei = endi - starti
    print("Итерационно при n = {} F(n) = {}, решено за {:.2f} секунд)".format(n, ite, timei))

    pyplot.ylabel('n')
    pyplot.xlabel('Время (в сек.)')
    pyplot.plot([timer], [n], 'ro', label='Рекурсивно')
    pyplot.plot([timei], [n], 'go', label='Итеративно')
    pyplot.legend()
    pyplot.show()
except ValueError:
    print('\nВведенный символ не является числом. Перезапустите программу и введите число.')

