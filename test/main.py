import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

x = 0.5 + np.arange(5)
y = [5, 6, 4, 3, 2]

graph_pos = [0.1, 0.1, 5, 5]

labels = ["Health", "Strength", "Defense", "Speed", "xp"]

fig, ax = plt.subplots()
ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7, label=labels)
ax.set(xlim=(0, 100), xticks=np.arange(1, 100),
       ylim=(0, 100), yticks=np.arange(1, 100), xlabel="Type", ylabel="Stats", position=graph_pos)

plt.show()