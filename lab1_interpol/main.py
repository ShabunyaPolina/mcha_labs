# Шабуня Полина лаб1 (вариант 10)

# f1(x) = cos(x); f2(x) = |x| - 1;
# [a; b] = [-3; 3]

from math import cos, factorial

import matplotlib.pyplot as plt


# вычисояет значение интерполяционного многочлена
def calc_p(xi, X, Y):
    res = 0
    for i in range(len(X)):
        mul = 1
        for j in range(len(X)):
            if i != j:
                mul *= (xi - X[j]) / (X[i] - X[j])
        res += Y[i] * mul
    return res


def f1(x):
    return cos(x)


def f2(x):
    return abs(x) - 1


# вычисляет значения функции f в точках xi
def fill_yi(f, X):
    Y = []
    for i in X:
        Y.append(f(i))
    return Y


# находит n равномерно расположенных на отрезке точек
def split_into_points(l_border, r_border, n):
    length = abs(l_border) + abs(r_border)
    step = length / (n - 1)
    next_point = l_border
    points_ = [next_point]
    for i in range(n - 1):
        next_point += step
        points_.append(next_point)
    return points_


def calc_actual_error(Y, Pn):
    max_error = 0
    for i in range(len(Y)):
        error = abs(Y[i] - Pn[i])
        if error > max_error:
            max_error = error
    return max_error


def find_rem(x, X, Y):
    rem = 1
    max_f = 0

    for i in range(len(X)):
        rem *= (x - X[i])
        if abs(Y[i]) > max_f:
            max_f = abs(Y[i])
    rem = abs(rem)

    rem /= factorial(len(X))
    rem *= max_f
    return rem


# границы заданного отрезка
LEFT_BORDER = -3
RIGHT_BORDER = 3

N = [2, 4, 6, 10, 20, 30]  # степени многочлена

# графики функций
points_f = split_into_points(LEFT_BORDER, RIGHT_BORDER, 30 + 1)

graph_f1 = plt.plot(points_f, fill_yi(f1, points_f))
grid1 = plt.grid(True)
plt.title('f1(x)=cos(x)')
plt.show()

graph_f2 = plt.plot(points_f, fill_yi(f2, points_f))
grid2 = plt.grid(True)
plt.title('f2(x)=|x| - 1')
plt.show()

# значения точек, отличных от точек, используемых при вычислении интерполяционных многочленов
rand_points = split_into_points(LEFT_BORDER, RIGHT_BORDER, 30 + 2)
rand_points.insert(int((30 + 2) / 2), 0)


def impl(f):
    for ni in N:
        print("Степень ", str(ni), ':')

        # n узлов, равномерно расположенных на отрезке [l_border; r_border]
        points = split_into_points(LEFT_BORDER, RIGHT_BORDER, ni + 1)
        print('X: ', points)

        # значения функций в найденных узлах
        yi = fill_yi(f, points)
        print('Y: ', yi)

        print('Точки для проверки полученного многочлена X*: ', rand_points)

        Yi = fill_yi(f1, rand_points)
        print('Значения функции в точках X*: ', Yi)

        # значения интерполяционных многочленов в узлах для проверки
        pn = []

        for x in rand_points:
            pn.append(calc_p(x, points, yi))

        # print('Значения интерполяционного многочлена в точках Х*: ', pn)
        #
        # # сравнение
        # for i in range(32):
        #     print('f(x): ', Yi[i], '\t', 'pn(x): ', pn[i])
        #
        # # фактическая погрешность
        # error = calc_actual_error(Yi, pn)
        # print('Фактическая погрешность: ', error)
        #
        # # графики функции и интерполяционного многочлена
        # plt.plot(points_f, fill_yi(f, points_f))
        # plt.plot(rand_points, pn)
        # plt.legend(['f(x)', 'interpolation polynom'])
        # plt.grid(True)
        # plt.xlabel(u'x')
        # plt.ylabel(u'y(x)')
        # plt.show()

        print()


impl(f1)
impl(f2)


# 3-я производная функции f(x) = cos(x)
def f1_3pr(x):
    return -cos(x)


# 5-я производная функции f(x) = cos(x)
def f1_5pr(x):
    return cos(x)


Y_3pr = fill_yi(f1_3pr, points_f)
Y_5pr = fill_yi(f1_5pr, points_f)

# остаток интерполирования в форме Лагранжа
max_rem = 0
for x in rand_points:
    rem = find_rem(x, points_f, Y_3pr)
    if rem > max_rem:
        max_rem = rem


print('Остаток интерполирования функции f(x)=cos(x) в форме Лагранжа при n=2: ', max_rem)

max_rem = 0
for x in rand_points:
    rem = find_rem(x, points_f, Y_5pr)
    if rem > max_rem:
        max_rem = rem
print('Остаток интерполирования функции f(x)=cos(x) в форме Лагранжа при n=4: ', max_rem)
