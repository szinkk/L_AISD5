# F(1) = G(1) = 1; F(n) = – 3*G(n–1), G(n) = F(n–1) , при n >=2


import time
from matplotlib import pyplot as plt
try:
    n = int(input("Введите число n>=2: "))
    while n < 2:
        n = int(input("Введите число n>=2: "))


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


    # Подсчёт времени выполнения рекурсивно
    start_time = time.time()
    f_rec = F(n)
    end_time = time.time()
    recursive_time = end_time - start_time

    # Подсчёт времени выполнения итеративно
    start_time = time.time()
    f_iter = Iteratively(n)
    end_time = time.time()
    iterative_time = end_time - start_time

    # Вывод
    print("F({}) = {} (рекурсивно в {:.6f} секунд)".format(n, f_rec, recursive_time))
    print("F({}) = {} (итеративно в {:.6f} секунд)".format(n, f_iter, iterative_time))

    # График
    recursive_times = []  # создание списков для дальнейшего построения таблицы
    recursive_values = []
    iterative_times = []
    iterative_values = []
    n_values = list(range(1, n + 1, +1))

    for n in n_values:  # заполнение списков данными
        start = time.time()
        recursive_values.append(F(n))
        end = time.time()
        recursive_times.append(end - start)

        start = time.time()
        iterative_values.append(Iteratively(n))
        end = time.time()
        iterative_times.append(end - start)

    table = []
    for i, n in enumerate(n_values):
        table.append([n, recursive_times[i], iterative_times[i], recursive_values[i], iterative_values[i]])
    print('{:<10}|{:<22}|{:<22}|{:<25}|{:<30}'.format('n', 'Время рекурсии (с)', 'Время итерации (с)',
                                                      'Значение рекурсии', 'Значение итерации'))  # вывод таблицы
    print('-' * 160)
    for j in table:
        print('{:<10}|{:<22}|{:<22}|{:<25}|{:<30}'.format(j[0], j[1], j[2], j[3], j[4]))

    plt.plot(n_values, recursive_times, label='Рекурсия')  # вывод графиков
    plt.plot(n_values, iterative_times, label='Итерация')
    plt.xlabel('n')
    plt.ylabel('Время (с)')
    plt.title('Сравнение рекурсивного и итерационного подхода')
    plt.legend()
    plt.show()

    print("\nРабота программы завершена.\n")
except ValueError:
    print("\nВведенное значение n не является число. Пожалуйста, перезапустите программу и введите число")