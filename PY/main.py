import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

# from packaging.version import parse as parse_version
# data to be plotted
x = np.arange(1, 11)
y = x * x

# plotting
plt.title("Line graph")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.plot(x, y, color="red")
plt.show()

# def main():
#     print('Hi,')
#
#
# if __name__ == '__main__':
#     main()
