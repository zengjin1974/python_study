import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.sans-serif"] = 'SimHei'
plt.rcParams["axes.unicode_minus"] = False

# config InlineBackend.figure_format = 'svg'

# fig = plt.figure()
# fig = plt.figure(figsize=(10, 8))

# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# ax4 = fig.add_subplot(2, 2, 4)

# ax1 = fig.add_subplot(1, 1, 1)

fig, axes = plt.subplots(2, 2)

x = np.arange(6)
y = np.arange(6)

axes[0, 0].plot(x, y)
axes[1, 1].bar(x, y)

plt.show()
