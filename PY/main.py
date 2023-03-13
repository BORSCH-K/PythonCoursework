import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

f = 16 # частота сигнала
fd = 1024 #частота дискретизации
ph = 0 # начальная фаза
k = fd/f # шаг
A = 1 # амплитуда
t = np.arange(0,k)
y = A * np.sin(2*np.pi*t/k+ph) # t = np.linspace(-n, n-1, 2*n) ,
fig, ax = plt.subplots()
fig1, ax1 = plt.subplots()
ax.plot(t/fd,y)
ax.grid()
ax.set_xlabel('t,c')
ax.set_ylabel('A')
CS = np.fft.fft(y)
AS = np.abs(CS)
FS = np.angle(CS)
ax1.set_xlabel('Сдвиг фазы')
ax1.set_ylabel('w,Гц')
ax1.plot(t*f,FS)
ax1.grid()
fig3, ax3 = plt.subplots()
ax3.stem(t*f,AS)
ax3.set_xlabel('Амплитуда')
ax3.set_ylabel('w , Гц')
ax3.grid()
z = np.fft.ifft(CS)
fig4,ax4 = plt.subplots()
ax4.plot(t/fd,z)
ax4.set_xlabel('t , c')
ax4.set_ylabel('A')
ax4.grid()
plt.show()

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

# def main():
#     print('Hi,')
#
#
# if __name__ == '__main__':
#     main()
