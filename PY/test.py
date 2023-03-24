import numpy as np
from scipy import fft
import matplotlib.pyplot as plt

rng = np.random.default_rng()  # одно число
# print(rng)
min_len = 1100  # prime length is worst case for speed
a = rng.standard_normal(min_len)  # массив чисел
print(a)
b = fft.fft(a)  # ДПФ
print(b)

# c = fft.next_fast_len(min_len, real=True)
# print(c)  # 93312
# d = fft.fft(a, min_len)
# print(d)

t = []
for i in range(1, 100):
    x = fft.next_fast_len(i, real=True)
    t.append(x)
    print(i, x)

# plt.plot(range(1, 100), t)
# plt.show()
# time_step = 0.05
# time_vec = np.arange(0, 100, time_step)
# sin(2*pi*f*t)


# mixed_tone = nice_tone + noise_tone

# f = np.arange(50, 16000, 150)  # частоты
# f = 150

# plt.plot(f, result_time)
# plt.show()

# timeit
# размер входного сигнала и время
# f = 16  # частота сигнала
# fd = 1024  # частота дискретизации
# ph = 0  # начальная фаза
# k = fd / f  # шаг
# A = 1  # амплитуда
# t = np.arange(0, k)
# y = A * np.sin(2 * np.pi * t / k + ph)

# start_time = time.monotonic()
# x = np.fft.fft(mixed_tone)
# for f in range(50, 16000):
#     y = np.sin(2 * np.pi * f * time_vec)
#     # y.append(0)
#     start_time = time.monotonic()
#     x = np.fft.fft(y)
#     t = time.monotonic() - start_time
#     # t = timeit.timeit(stmt=np.fft.fft(y), number=1)
#     print(t)
#     result_time.append(t)
#
# print(result_time)

# nice_tone = generate_sine_wave(400, SAMPLE_RATE, DURATION)
# noise_tone = generate_sine_wave(4000, SAMPLE_RATE, DURATION)
# # noise_tone = noise_tone * 0.3


# Генерируем волну с частотой 2 Гц, которая длится 5 секунд
# x, y = generate_sine_wave(2, SAMPLE_RATE, DURATION)

# fig, ax = plt.subplots()
# ax.plot(result, [1, 4, 2, 3])  # Plot some data on the axes.


# fig, ax = plt.subplots()
# fig1, ax1 = plt.subplots()
# ax.plot(t / fd, y)
# ax.grid()
# ax.set_xlabel('t,c')
# ax.set_ylabel('A')
# CS = np.fft.fft(y)
# AS = np.abs(CS)
# FS = np.angle(CS)
# ax1.set_xlabel('Сдвиг фазы')
# ax1.set_ylabel('w,Гц')
# ax1.plot(t * f, FS)
# ax1.grid()
# fig3, ax3 = plt.subplots()
# ax3.stem(t * f, AS)
# ax3.set_xlabel('Амплитуда')
# ax3.set_ylabel('w , Гц')
# ax3.grid()
# z = np.fft.ifft(CS)
# fig4, ax4 = plt.subplots()
# ax4.plot(t / fd, z)
# ax4.set_xlabel('t , c')
# ax4.set_ylabel('A')
# ax4.grid()
# plt.show()

# from packaging.version import parse as parse_version
# data to be plotted
# x = np.arange(1, 11)
# y = x * x
#
# # plotting
# plt.title("Line graph")
# plt.xlabel("X axis")
# plt.ylabel("Y axis")
# plt.plot(x, y, color="red")
# plt.show()
