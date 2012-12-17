#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pylab
import numpy as np
fig = pylab.figure(figsize=(2., 1.5))
ax = pylab.gca()
pylab.subplots_adjust(bottom=0.2)
pylab.plot(np.random.randn(50))
pylab.grid()
pylab.setp(ax.get_xticklabels(), visible=False)
pylab.setp(ax.get_yticklabels(), visible=False)
pylab.xlabel('time')
pylab.ylabel('strain')
fig.patch.set_alpha(0)
ax.patch.set_alpha(0)
ax.set_alpha(0)
pylab.savefig('whitenoise.pdf')
