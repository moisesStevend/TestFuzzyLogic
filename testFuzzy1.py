# -*- coding: utf-8 -*-
"""
Created on Fri Jul  1 21:01:18 2016

@author: meza
"""

import neurolab as nl
import numpy as np

net = nl.net.newff([[0,1]] * 3, [4,2])

net.save("test.net")

net = nl.load("test.net")
# show layer weights and biases
for i in range(0,len(net.layers)):
    print "Net layer", i
    print net.layers[i].np['w']
    print "Net bias", i
    print net.layers[i].np['b']

#try setting layer weights
net.layers[0].np['w'][:] = np.array ([[0,1,2],  
                                     [3,4,5],  
                                     [4,5,6],  
                                     [6,7,8]]
                                     )


# show layer weights and biases 
for i in range(0,len(net.layers)):
    print "Net layer", i
    print net.layers[i].np['w']
    print "Net bias", i
    print net.layers[i].np['b']