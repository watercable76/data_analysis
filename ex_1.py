"""
Author: Nicholas Cable, el cablecito
Date Created: 1/13/2021
Purpose: Work with an example data set using matplotlib,
        and display some graphs with the data.
Last updated: ...
"""

# import matplotlib.pyplot as plt
# import numpy as np

# fig, ax = plt.subplots()
# ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
# plt.plot([1, 2, 3, 4], [1, 4, 2, 3])

# # create an empty figure w/o aces
# fig = plt.figure()

# # a figure with a single axes
# fig, ax = plt.subplots()

# # a figure with a 2x2 grid of axes
# fig, axs = plt.subplots(2, 2)


import matplotlib.pyplot as plt
from matplotlib.collections import EventCollection
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)

# create random data
xdata = np.random.random([2, 10])

# split the data into two parts
xdata1 = xdata[0, :]
xdata2 = xdata[1, :]

# sort the data so it makes clean curves
xdata1.sort()
xdata2.sort()

# create some y data points
ydata1 = xdata1 ** 2
ydata2 = 1 - xdata2 ** 3

# plot the data
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(xdata1, ydata1, color='tab:blue')
ax.plot(xdata2, ydata2, color='tab:orange')

# create the events marking the x data points
xevents1 = EventCollection(xdata1, color='tab:blue', linelength=0.05)
xevents2 = EventCollection(xdata2, color='tab:orange', linelength=0.05)

# create the events marking the y data points
yevents1 = EventCollection(ydata1, color='tab:blue', linelength=0.05,
                           orientation='vertical')
yevents2 = EventCollection(ydata2, color='tab:orange', linelength=0.05,
                           orientation='vertical')

# add the events to the axis
ax.add_collection(xevents1)
ax.add_collection(xevents2)
ax.add_collection(yevents1)
ax.add_collection(yevents2)

# set the limits
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])

ax.set_title('line plot with data points')

# display the plot
plt.show()


# Open the file
with open('life-expectancy.csv') as data:
    # Skip the header line
    next(data)

    # Data to be used in comparisons and outputs
    lfh = 0
    lfl = 999
    hc = ''
    lc = ''
    hy = 0
    ly = 0
    avg = 0

    right = 'empty'

    # Prompt the user to see if they want to check a certain year
    y_n = input(
        'Would you like to see a certain year? Type \'yes\' for yes and \'no\' for no. ')

    if y_n.lower() == 'yes':
        # Prompt the user for a year
        choice = int(input('Please enter a year you would like to check: '))

    for line in data:
        cl = line.strip().split(',')
        country = cl[0]
        code = cl[1]
        year = int(cl[2])
        life_expec = float(cl[3])

        # check to see if the user did pick a year

        if y_n.lower() != 'yes':
            # find new life expect high
            if life_expec > lfh:
                lfh = life_expec
                hc = country
                hy = year
            # find new life expect low
            if life_expec < lfl:
                lfl = life_expec
                lc = country
                ly = year
        else:
            # check to see if the year input is the year in the database
            if choice == year:
                # Make sure data is printing out correctly
                right = 'right_stuff'
                # find new life expect high
                if life_expec > lfh:
                    lfh = life_expec
                    hc = country
                    hy = year
                # find new life expect low
                if life_expec < lfl:
                    lfl = life_expec
                    lc = country
                    ly = year

    # print out the highs and lows
    print(f'The highest life expect was {lfh} in the year {hy} in the country {hc}.')
    print(f'The highest life expect was {lfl} in the year {ly} in the country {lc}.')
    print(right, choice)
