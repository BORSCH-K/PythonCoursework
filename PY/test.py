f = open('test.txt', 'r')

temp_freq, t = map(float, f.readline().split())
print(temp_freq, t)
f.close()
# print(freq[i], time[i])
# import numpy as np
# import scipy as sp
# from scipy import fft
# import matplotlib.pyplot as plt
# import timeit
#
# SAMPLE_RATE = 44100  # Гц частота дискретизации
# DURATION = 5  # Секунды
#
#
# # freq - частота, sample_rate - частота дискретизации, duration - секунды
# def generate_sine_wave(freq, sample_rate, duration):
#     x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
#     # 2pi для преобразования в радианы
#     y = np.sin((2 * np.pi) * x * freq)
#     return x, y
#
#
# def generate_signal(size_y, freq):
#     # y = np.arange(0, size_y)
#     x = np.arange(0, size_y)
#     y = np.sin((2 * np.pi) * x * freq)
#     return y
#
#
# def index(element, a):
#     # print("size: ", a, element)
#     if (element-a-1000 == 0):
#         # print("a - 1: ", a-1)
#         return a-1
#     else:
#         # print("element-1000: ", element-1000)
#         return element-1000
#
#
# result_time = []
# locale_rate = 1000
# k = []
# for i in range(0, 125):
#     # start_time = time.monotonic()
#     # rng = np.random.default_rng()
#     # min_len = 1100
#     # y = rng.standard_normal(min_len)
#     y = generate_signal(locale_rate, 160)
#     # np.fft.fft(np.arange(0, locale_rate))
#     t = timeit.timeit(stmt='np.fft.fft(y)', globals={**globals(), **locals()}, number=10)
#
#     x = fft.next_fast_len(locale_rate, real=True)
#     k.append(x)
#
#     result_time.append(t)
#     locale_rate += 1
#     # print(i, t)
#
# rate_point = []
# time_point = []
# rate_point.append(k[0])
# time_point.append(result_time[0])
# print(rate_point, time_point, k[0] - 1000)
# j = 0
# for i in range(0, locale_rate - 1000):  # 125
#     if k[i] != rate_point[j]:
#         j += 1
#         rate_point.append(k[i])
#         time_point.append(result_time[index(k[i], len(result_time))])
#     print(i, rate_point, time_point, index(k[i], len(result_time)))
#
# print(k)
# plt.plot(range(1000, locale_rate), result_time)
# plt.plot(rate_point, time_point, 'o')
# plt.show()

# def main():
#
# if __name__ == '__main__':
#     main()

# for i in range(0, 3):
#     print(i)

# def generate_sine_wave(freq, sample_rate, duration):
#     x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
#     # 2pi для преобразования в радианы
#     y = np.sin((2 * np.pi) * x * freq)
#     return x, y
#
#
# def generate_signal(size_y, freq):
#     # y = np.arange(0, size_y)
#     x = np.arange(0, size_y)
#     y = np.sin((2 * np.pi) * x * freq)
#     return y
# import numpy as np
# from scipy import fft
# import matplotlib.pyplot as plt
#
# rng = np.random.default_rng()  # одно число
# # print(rng)
# min_len = 1100  # prime length is worst case for speed
# a = rng.standard_normal(min_len)  # массив чисел
# print(a)
# b = fft.fft(a)  # ДПФ
# print(b)
#
# # c = fft.next_fast_len(min_len, real=True)
# # print(c)  # 93312
# # d = fft.fft(a, min_len)
# # print(d)
#
# t = []
# for i in range(1, 100):
#     x = fft.next_fast_len(i, real=True)
#     t.append(x)
#     print(i, x)
