# Importing packages
import matplotlib.pyplot as plt

# Importing packages
import matplotlib.pyplot as plt

plt.ylabel("Controller Latency (ms) ")
plt.xlabel("No. of Switches")

# Define data values
x = [60, 50, 40, 30, 20, 10, 0]
ONOS = [58.23, 48.87, 42.30, 40.20, 35.22, 27.10, 12.30]
Floodlight = [51.20, 49.44, 44.33, 41.20, 33.12, 16.20, 14.78]
OpenDayLight = [58.9, 46.44, 37.20, 33.33, 27.20, 21.20, 16.78]
RYU = [33.98, 31.12, 30.20, 28.73, 26.20, 24.27, 11.78]


# Plot ONOS line graph
plt.plot(x, ONOS)

# Plot Floodlight on the same graph
plt.plot(x, Floodlight)


# Plot OpenDayLight on the same graph
plt.plot(x, OpenDayLight)

# Plot RYU on the same graph
plt.plot(x, RYU)


location = 0 
legend_drawn_flag = True
plt.legend(["ONOS", "Floodlight", "OpenDayLight", "RYU"], loc=0, frameon=legend_drawn_flag)

plt.show()
