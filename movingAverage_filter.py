import matplotlib.pyplot as plt #version 3.5.1
import pandas as pd #version 1.3.5

dataFrame = pd.read_csv("gaze_positions_on_surface_Surface 1.csv")

window_size = 9

# Simple Moving Average for x values
x_SMA=dataFrame['x_scaled'].rolling(window = window_size).mean()
# Exponential Moving Average for x values
x_EMA=dataFrame['x_scaled'].ewm(span = window_size, adjust = False).mean()
# Cumulative Moving Average for x values
x_CMA=dataFrame['x_scaled'].expanding(min_periods = window_size).mean()


# Simple Moving Average for y values
y_SMA=dataFrame['y_scaled'].rolling(window = window_size).mean()
# Exponential Moving Average for y values
y_EMA=dataFrame['y_scaled'].ewm(span = window_size, adjust = False).mean()
# Cumulative Moving Average for y values
y_CMA= dataFrame['y_scaled'].expanding(min_periods = window_size).mean()

dataFrame['world_timestamp'] = dataFrame['world_timestamp'] - 403281.16369
plt.grid(True)

# before
plt.plot(dataFrame['world_timestamp'], dataFrame['x_scaled'], label = 'x')

# after
plt.plot(dataFrame['world_timestamp'], x_SMA, label = 'x_SMA' + str(window_size))
plt.plot(dataFrame['world_timestamp'], x_EMA, label = 'x_EMA' + str(window_size))
plt.plot(dataFrame['world_timestamp'], x_CMA, label = 'x_CMA' + str(window_size))

""" 
# before 
plt.plot(dataFrame['world_timestamp'], dataFrame['y_scaled'], label = 'y')
# after
plt.plot(dataFrame['world_timestamp'], y_EMA, label = 'y_EMA' + str(window_size))
plt.plot(dataFrame['world_timestamp'], y_SMA, label = 'y_SMA' + str(window_size))
plt.plot(dataFrame['world_timestamp'], y_CMA, label = 'y_CMA' + str(window_size))
"""
plt.legend(loc=2)

plt.show()
