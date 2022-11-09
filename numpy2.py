# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
from decimal import Decimal, getcontext


getcontext().prec = 6

# Функция работает очень долго, потому что
# каждый новый факториал считается с 1, а не через предыдущий
# @np.vectorize
# def factorial(x):
#     if x == 0:
#         return Decimal(1)
#     return factorial(x-1)*Decimal(x)


def Factorial(arr):
    n = Decimal('1')
    factorial = np.array([Decimal(1)])
    for x in arr[1:]:
        n *= x
        factorial = np.append(factorial, n)
    return factorial


def Puasson(la, N):
    if la < 0:
        raise ValueError("Lambda must be positive")
    # numpy_arr = np.arange(Decimal(N), dtype='float64')
    numpy_arrD = np.asarray([Decimal(i) for i in range(N)])
    return la ** numpy_arrD * Decimal(-la).exp() / Factorial(numpy_arrD)


def Moment(arr, k=1):
    if k < 0:
        raise ValueError('"k" must be positive')
    elif k % 1:
        raise ValueError('"k" must be integer')
    elif not isinstance(arr, np.ndarray):
        raise ValueError('Wrong array format')
    return np.sum(arr * np.arange(len(arr)) ** k)


def Mean(arr):
    return Moment(arr, 1)


def Diviation(arr):
    return Moment(arr, 2) - Moment(arr, 1) ** 2


def Plotter(arr):
    plt.plot(arr)
    plt.show()


def Test(x, answer, error=0.1):
    if abs(x - answer) <= error:
        return "cовпадает в пределах погрешности " + str(error)
    return "не cовпадает в пределах погрешности " + str(error)


if __name__ == '__main__':
    la = 50  # int(input())
    N = 100  # int(input())
    k = 2  # int(input())
    error = 0.1  # float(input())
    arr = Puasson(la, N)
    Plotter(arr)
    print("Начальный момент случайной великичны для k =",
          k, "равен", Moment(arr, k))
    print("Среднее значение равно", Mean(arr), "оно",
          Test(Mean(arr), la), "с реальным значением", la)
    print("Дисперсия случайной величины равна", Diviation(arr),
          "она", Test(Diviation(arr), la), "с реальным значением", la)
