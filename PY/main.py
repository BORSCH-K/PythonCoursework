import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import timeit

SAMPLE_RATE = 44100  # Гц частота дискретизации
DURATION = 5  # Секунды


# freq - частота, sample_rate - частота дискретизации, duration - секунды
def generate_sine_wave(freq, sample_rate, duration):
    x = np.linspace(0, duration, sample_rate * duration, endpoint=False)
    # 2pi для преобразования в радианы
    y = np.sin((2 * np.pi) * x * freq)
    return x, y


def generate_signal(size_y, freq):
    # y = np.arange(0, size_y)
    x = np.arange(0, size_y)
    y = np.sin((2 * np.pi) * x * freq)
    return y


result_time = []
locale_rate = 1000
for i in range(0, 20):
    # start_time = time.monotonic()
    y = generate_signal(locale_rate, 160)
    # np.fft.fft(np.arange(0, locale_rate))
    t = timeit.timeit(stmt='np.fft.fft(y)', globals={**globals(), **locals()}, number=10000)

    result_time.append(t)
    locale_rate += 1
    print(t)

plt.plot(range(1000, locale_rate), result_time)
plt.show()

# def main():
#
# if __name__ == '__main__':
#     main()
