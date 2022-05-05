import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10, 0.08)
y = np.sin(x)
y_data = y + np.random.normal(0, 0.1, 250)

plt.figure('test1')
plt.subplot(2, 2, 1)
plt.plot(x, y, color='r')
plt.subplot(2, 2, 2)
plt.plot(x, y, '*')
plt.plot(x, y_data, '.')
plt.xlim(-5, 5)
plt.ylim(-1, 1)
plt.scatter(x, y_data)

fig = plt.figure()
ax = fig.add_subplot(1, 2, 1)
ax.set_title('Shopping age - bar chart')
ax.set_ylabel('numbers')

xticks = np.arange(3)
bar_width = 0.5
ax.set_xticks(xticks + bar_width)
plt.show()
