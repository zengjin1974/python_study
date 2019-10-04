import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# plt.rcParams["font.sans-serif"] = 'SimHei'
plt.rcParams["axes.unicode_minus"] = False

# config InlineBackend.figure_format = 'svg'

fig = plt.figure()
# fig = plt.figure(figsize=(10, 8))

# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# ax4 = fig.add_subplot(2, 2, 4)

ax1 = fig.add_subplot(1, 1, 1)
plt.xlabel("Month")
plt.ylabel("Register")

plt.xticks(np.arange(9), ["Jan", "Feb", "Mar",
                          "Apr", "May", "Jun",
                          "Jul", "Aug", "Sep"])

plt.yticks(np.arange(1000, 7000, 1000),
           ["1000", "2000", "3000",
            "4000", "5000", "6000"])

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([866, 2335, 5710, 6482, 6120, 1605, 3813, 4428, 4631])

plt.plot(x, y)

# fig, axes = plt.subplots(2, 2)
#
# x = np.arange(6)
# y = np.arange(6)
#
# axes[0, 0].plot(x, y)
# axes[1, 1].bar(x, y)

plt.show()
