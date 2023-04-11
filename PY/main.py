import math
import numpy as np
import scipy as sp
from scipy import fft
import matplotlib.pyplot as plt
import timeit

INITIAL_FREQ = 1000  # начальная частота
LEN_RANGE = 201  # длина диапазона
N = 1000 # количество повторений fft


def time(i):
    y = [0] * (i)  # массив с длиной от 1000 до 1000+LEN_RANGE-1
    t = timeit.timeit(stmt='np.fft.fft(y)', globals={**globals(), **locals()}, number=N)
    print(i, t)
    return t


def nfl(i):
    x = fft.next_fast_len(i, real=True)  # нахождение благоприятной точки
    return x


def M_(x):  # среднее значение
    # x - массив чисел
    return sum(x) / len(x)


def D_(x, M):  # среднеквадратичное значение
    # x - массив чисел
    # M - среднее значение
    for i in range(0, len(x)):
        sum_ = (x[i] - M) ** 2
    return math.sqrt(sum_ / (len(x) - 1))


time_fft = []  # время на ДПФ
locale_rate = 1000  # начальная частота, изменяемая
k_points = []  # список точкей с наилучшей частотой

X = []  # время для ? частоты * 10
M = []  # среднее значение х
D = []  # среднеквадратичное отклонение
for range_element in range(INITIAL_FREQ, LEN_RANGE+INITIAL_FREQ):  # range_element - элемент диапазона
    x = []
    for i in range(0,10):
        x.append(time(range_element))
    X.append(x)
    M.append(M_(x))
    j = range_element - INITIAL_FREQ
    time_fft.append(M[j])
    D.append((D_(x, M[j])))
    print(range_element, M[j], D[j], (D[j]/M[j]*100))
    # print(x)

k = INITIAL_FREQ  # текущая частота
while k < (LEN_RANGE + INITIAL_FREQ): # [1000, 1024, 1080, 1125, 1152, 1200]
    k_temp = nfl(k)
    k_points.append(k_temp)
    k = k_temp + 1
print(k_points)

k_time = []
for i in range(0, len(k_points)):
    k_time.append(time_fft[k_points[i]- INITIAL_FREQ])
print(k_time)
# for i in range(0, len(k_points)):
#     x = []
#     print(k_points[i])
#     for j in range(0, 10):
#         x.append(time(k_points[i]))
#     X.append(x)
#     M.append(M_(x))
#     D.append((D_(x, M[i])))
#
#     print(i, M[i], D[i])
#     print(x)
print(time_fft) # средние значения
plt.plot(range(INITIAL_FREQ, INITIAL_FREQ + LEN_RANGE), time_fft)
plt.plot(k_points, k_time, 'o')
plt.show()
