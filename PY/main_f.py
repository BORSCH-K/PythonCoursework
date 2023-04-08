freq = [0] * 1001
time = [0.] * 1001

f = open('data-322.txt', 'r')
for i in range(0, 1000):  # запись данных
    # print(f.readline())
    temp_freq, time[i] = map(float, f.readline().split())
    freq[i] = int(temp_freq)
    # print(freq[i], time[i])
time[1000] = 1.1059521999998196
freq[1000] = 2000
f.close()

# нахождение быстрых точек
fast_freq = []

# наилучшие точки
k = [1000, 1024, 1080, 1125, 1152, 1200, 1215, 1250, 1280, 1296, 1350, 1440,
     1458, 1500, 1536, 1600, 1620, 1728, 1800, 1875, 1920, 1944, 2000]
index = [0] * len(k)  # индексы наилучших точек
for i in range(0, len(k)):
    index[i] = k[i] - 1000
print(index)
s_time = [0]*(len(k)-1)
difference = [0]*(len(k)-1)
for i in range(0, len(k) - 1): # средние числа и их разность
    print(i, index[i])
    print(time[index[i]], time[index[i + 1]])
    s_time[i] = (time[index[i]] + time[index[i + 1]]) / 2
    difference[i] = abs(time[index[i]] - time[index[i + 1]])
    print(s_time[i])
    print(difference[i])
