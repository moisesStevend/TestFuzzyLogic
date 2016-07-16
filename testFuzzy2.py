# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 22:10:02 2016

@author: meza
"""

import skfuzzy as fuzz
import numpy as np
import matplotlib.pyplot as plt

x=np.arange(11)
print x

mfx=fuzz.trimf(x, [0, 5,10])
print mfx

plt.plot(x,mfx)
plt.grid('on')
plt.show()