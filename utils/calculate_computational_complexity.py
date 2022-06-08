import time

import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

num_points = 500
times_x = []
times_y = []
for i in range(num_points):
    def linear_code():
        counter = 0
        total_time = 0
        for _ in range(i):
            start = time.perf_counter()
            counter += 1
            end = time.perf_counter()
            total_time += end - start
        return total_time

    def quadratic_code():
        counter = 0
        total_time = 0
        for _ in range(i):
            for __ in range(i):
                start = time.perf_counter()
                counter += 1
                end = time.perf_counter()
                total_time += end - start
        return total_time

    times_x.append(i)
    times_y.append(linear_code())


def linear(x, a, b):
    return a + b * x
    # For actual linear data
    # [1.46328317e-07 2.88419678e-08]
    # [[ 2.55200851e-14 -7.66368774e-17]
    #  [-7.66368774e-17  3.07161798e-19]]

    # For quadratic data
    # [-3.75216320e-03  4.49931952e-05]
    # [[ 9.78459556e-08 -2.93831695e-10]
    #  [-2.93831695e-10  1.17768214e-12]]


def quadratic(x, a, b, c):  # , d, e):
    return a + b * x + c * x**2  # + d * x * np.log(e * x)
    # For linear data
    # [8.34189259e-07 1.73657639e-08 3.66456971e-11]
    # [[ 4.31582032e-14 -3.45610655e-16  5.76594362e-19]
    #  [-3.45610655e-16  3.69853736e-18 -6.94692000e-21]
    #  [ 5.76594362e-19 -6.94692000e-21  1.39216836e-23]]

    # For actual quadratic data
    # [ 1.12806298e-03 -1.94547137e-05  1.46508901e-07]
    # [[ 2.53088638e-07 -2.02673237e-09  3.38126843e-12]
    #  [-2.02673237e-09  2.16889879e-11 -4.07381743e-14]
    #  [ 3.38126843e-12 -4.07381743e-14  8.16396279e-17]]

popt, pcov = curve_fit(quadratic, times_x, times_y)
print(popt)
print(pcov)

plt.scatter(times_x, times_y, label="data")

fit_x = np.linspace(1, num_points, num_points)
# fit_1 = linear(fit_x, popt[0], popt[1])
fit_1 = quadratic(fit_x, popt[0], popt[1], popt[2])  # , popt[3], popt[4])
# fit_2 = curve(fit_x, popt[0], popt[1], popt[2])  # , 0, popt[4])
# fit_3 = curve(fit_x, popt[0], 0, 0, popt[3], popt[4])
plt.plot(fit_x, fit_1, 'r', label="fit 1")
# plt.plot(fit_x, fit_2, 'm', label="fit 2")
# plt.plot(fit_x, fit_3, 'g', label="fit 3")
plt.legend()
plt.show()
