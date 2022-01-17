import matplotlib.pyplot as plt #version 3.5.1
import pandas as pd #version 1.3.5
import scipy.signal #used for signal processing #version 1.7.3

# Read the csv file into DataFrame. (csv: comma-separated values)
dataFrame = pd.read_csv("gaze_positions_on_surface_Surface 1.csv")

# window:the pattern of neighboring inputs that slides from input to input across the entire signal.
# to change the smothness we can change the window size
# in median filter 'Each element of kernel_size should be odd'

window_size = 9
# window_size = 15
# window_size = 35

# 1st entry of world_timestamp for my experiment was 403281.16369
# converting the pupil time to system time by subtraction of the 1st entry of world_timestamp
dataFrame['world_timestamp'] = dataFrame['world_timestamp'] - 403281.16369

# medfilt will perform a median filter on an N-dimensional array. the kernel size is the window size.
median_for_x = scipy.signal.medfilt(dataFrame['x_scaled'], window_size)
median_for_y = scipy.signal.medfilt(dataFrame['y_scaled'], window_size)


plt.grid(True)

# ploting the values before application
plt.plot(dataFrame['world_timestamp'], dataFrame['x_scaled'], label = 'actual_x')
# ploting the values after application
plt.plot(dataFrame['world_timestamp'], median_for_x, label = 'median_for_x' + '_' + str(window_size))

""" 
# representing the values before application 
plt.plot(dataFrame['world_timestamp'], dataFrame['y_scaled'], label = 'actual_y')
# representing the values after application
plt.plot(dataFrame['world_timestamp'], median_for_y, label = 'median_for_y' + '_' + str(window_size))

"""


# location of table
plt.legend(loc=2)

plt.show()
