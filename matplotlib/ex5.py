# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 11:19:00 2017

@author: Jonas Lindemann
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.0, 2*np.pi, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

#plt.plot(x, y1, 'r-', x, y2, 'b-', linewidth=4.0)
line1, line2 = plt.plot(x, y1, 'r-', x, y2, 'b-')
line1.set_linewidth(4.0)
line2.set_linewidth(8.0)

plt.show()