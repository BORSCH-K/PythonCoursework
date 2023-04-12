import matplotlib.pyplot as plt

freq = [0] * 201
time = [0.] * 201

f = open('data-330.txt', 'r')
lines = f.readlines()
i = 0
for j in range(10, 2211, 11):  # запись данных
    #     # print(f.readline())
    temp_freq, time[i], a, d = map(float, lines[j].split())
    freq[i] = int(temp_freq)
    print(freq[i], time[i])
    i += 1
# есть же точки с неудовлетворительной точностью

# для 322:
# time[51] = 1.2438040850000003

# для 330:
# time[15] = 1.1773835055
# time[34] = 1.2441199561500005

# для 506:
# time[49] = 1.2861662750000002

f.close()

# нахождение быстрых точек
fast_t = []

# наилучшие точки
k = [1000, 1024, 1080, 1125, 1152, 1200]
index = [0] * len(k)  # индексы наилучших точек
for i in range(0, len(k)):
    index[i] = k[i] - 1000
print(index)
for i in index:
    fast_t.append(time[i])
    print(i, time[i])
print(fast_t)
s_time = [0] * (len(k) - 1)  # среднее время между н.частотами
# difference = [0] * (len(k) - 1)  # разность времени между н.частотами
diapason = [0] * (len(k) - 1)  # диапазон для быстрых частот
for i in range(0, len(k) - 1):  # средние числа и их разность
    # print(i, index[i])
    # print(time[index[i]], time[index[i + 1]])
    s_time[i] = (time[index[i]] + time[index[i + 1]]) / 2
    #     difference[i] = abs(time[index[i]] - time[index[i + 1]])
    #
    #     # диапазон
    diapason[i] = max(time[index[i]], time[index[i + 1]]) * 1.1  # + 0.5 * difference[i] # от максимального
#     # diapason[i] = s_time[i] + 0.2 * difference[i]  # от среднего
#     print(s_time[i], difference[i])
#
j = -1
# диапазон = +20% от разницы к максимальному значению (или среднему?)
speed_f = []  # частота б.точек
speed_t = []  # время б.точек
for i in range(0, 201):
    if (freq[i] in k) == 0:  # если частота не принадлежит нфл
        if time[i] <= diapason[j]:
            speed_t.append(time[i])
            speed_f.append(freq[i])
            print(freq[i], time[i])
    else:
        j += 1

print("Количество быстрых точек: ", len(speed_f))
print("Количество NFL-точек: ", len(k))
print("Общее время выполнения: ", sum(time))
print("Среднее время выполнения операции: ", sum(time) / 201)

# plt.plot(freq, time)
# plt.plot(k, fast_t, 'o')
# plt.plot(speed_f, speed_t, 'o')
# plt.show()
