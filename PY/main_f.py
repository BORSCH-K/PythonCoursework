import matplotlib.pyplot as plt

freq = [0] * 1001
time = [0.] * 1001

f = open('data-322.txt', 'r')
for i in range(0, 1000):  # запись данных
    # print(f.readline())
    temp_freq, time[i] = map(float, f.readline().split())
    freq[i] = int(temp_freq)
    # print(freq[i], time[i])
# temp_freq, time[1000] = map(float, f.readline(1288).split())
# freq[1000] = int(temp_freq)
time[1000] = 1.1059521999998196
freq[1000] = 2000
f.close()

# нахождение быстрых точек
fast_t = []

# наилучшие точки
k = [1000, 1024, 1080, 1125, 1152, 1200, 1215, 1250, 1280, 1296, 1350, 1440,
     1458, 1500, 1536, 1600, 1620, 1728, 1800, 1875, 1920, 1944, 2000]
index = [0] * len(k)  # индексы наилучших точек
for i in range(0, len(k)):
    index[i] = k[i] - 1000
print(index)
for i in index:
    fast_t.append(time[i])
    print(i, time[i])
print(fast_t)
s_time = [0] * (len(k) - 1)  # среднее время между н.частотами
difference = [0] * (len(k) - 1)  # разность времени между н.частотами
diapason = [0] * (len(k) - 1)  # диапазон для быстрых частот
for i in range(0, len(k) - 1):  # средние числа и их разность
    # print(i, index[i])
    # print(time[index[i]], time[index[i + 1]])
    s_time[i] = (time[index[i]] + time[index[i + 1]]) / 2
    difference[i] = abs(time[index[i]] - time[index[i + 1]])
    diapason[i] = max(time[index[i]], time[index[i + 1]]) + 0.2 * difference[i] # от максимального
    # diapason[i] = s_time[i] + 0.2 * difference[i]  # от среднего
    print(s_time[i], difference[i])

j = -1
# диапазон = +20% от разницы к максимальному значению (или среднему?)
speed_f = []  # частота б.точек
speed_t = []  # время б.точек
for i in range(0, 1001):
    if (freq[i] in k) == 0:  # если частота не принадлежит нфл
        if time[i] <= diapason[j]:
            speed_t.append(time[i])
            speed_f.append(freq[i])
            print(freq[i], time[i])
    else:
        j += 1

plt.plot(freq, time)
plt.plot(k, fast_t, 'o')
plt.plot(speed_f, speed_t, 'o')
plt.show()
