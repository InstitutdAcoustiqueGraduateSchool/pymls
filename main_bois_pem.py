#! /usr/bin/env python
# -*- coding:utf8 -*-
#
# main_pem_bois.py
#
# This file is part of pypw, a software distributed under the MIT license.
# For any question, please contact one of the authors cited below.
#
# Copyright (c) 2017
# 	Olivier Dazel <olivier.dazel@univ-lemans.fr>
# 	Mathieu Gaborit <gaborit@kth.se>
# 	Peter Göransson <pege@kth.se>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#

from matplotlib import pyplot as plt
import numpy as np
from numpy.lib.scimath import sqrt

from pypw import from_yaml, Solver, Layer, backing


freq=20
d_pem=200e-3
d_wood=2e-2
theta=30

foam = from_yaml('materials/foam2.yaml')
wood = from_yaml('materials/bois.yaml')

S = Solver()
# S.media = [Air, foam, wood]
S.layers = [
    Layer(wood, d_wood),
    Layer(foam, d_pem),
]
S.backing = backing.rigid

result = S.solve(freq, theta)
R_recursive = result[0]['R'][0]

print("R_recursive=")
print(R_recursive)
#


