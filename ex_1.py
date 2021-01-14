"""
Author: Nicholas Cable, el cablecito
Date Created: 1/13/2021
Purpose: Work with an example data set using matplotlib,
        and display some graphs with the data.
Last updated: ...
"""

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
plt.plot([1, 2, 3, 4], [1, 4, 2, 3])

# create an empty figure w/o aces
fig = plt.figure()

# a figure with a single axes
fig, ax = plt.subplots()

# a figure with a 2x2 grid of axes
fig, axs = plt.subplots(2, 2)
