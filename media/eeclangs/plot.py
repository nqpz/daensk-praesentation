#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 22}

plt.rc('font', **font)

labels = 'German', 'English', 'French', 'Italian', 'Dutch', 'Danish'
sizes = [61949200, 59773000, 58189200, 56479000, 20008800, 5124000]

fig, ax = plt.subplots()
explode = (0, 0, 0, 0, 0, 0.2)
colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(sizes)))
ax.pie(sizes, colors=colors, explode=explode, labels=labels, autopct='%1.1f%%', startangle=0)

plt.show()
