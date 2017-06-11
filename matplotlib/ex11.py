# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 11:19:00 2017

@author: Jonas Lindemann
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.0, 2*np.pi, 0.1)
y = np.sin(x)


plt.figure(1)
plt.xlabel("x")
plt.ylabel("y")
plt.annotate('max', xy=(np.pi/2, 1), xytext=(np.pi/2, 0.5),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
plt.plot(x, y, 'r-')

plt.show()