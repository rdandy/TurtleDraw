#! /usr/bin/env python

from turtle import *

for steps in range(100):
    for c in ('blue', 'red', 'green'):
        color(c)
        forward(steps)
        right(30)

mainloop()
