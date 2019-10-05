# 绘制气泡图

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

plt.subplot(1, 1, 1)

x = np.array([5.5, 6.6, 8.1, 15.8, 19.5, 22.4, 28.3, 28.9])
y = np.array([2.38, 3.85, 4.41, 5.67, 5.44, 6.03, 8.15, 6.87])

colors = y * 10
area = y * 100

plt.scatter(x, y, c=colors, marker="o", s=area)

plt.title("Jan-Aug Temperature vs Bear Sale", loc="center")

for a, b in zip(x, y):
    plt.text(a, b, b, ha='center', va="center", fontsize=10, color="white")

plt.xlabel('Temperature')
plt.ylabel('Bear Sale')

plt.grid(False)

plt.show()

