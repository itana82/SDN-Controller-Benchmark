from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
import numpy as np
import mpl_toolkits.axisartist as axisartist

x = np.arange(4)
#flowsL = [28335.38, 37755.46, 3416.99, 47257.7]
#flowsT = [30094.09, 133285.65, 2986.43, 33568.73]

flowsL = [1802.2, 28335.38, 37755.46, 3416.99]
flowsT = [3052.9, 3009.09, 1332.65, 2986.43]

def seconds(x, pos):
    'The two args are the value and tick position'
    return '%1.1f' % (x * 1e-3)


formatter = FuncFormatter(seconds)

fig, ax = plt.subplots()
ax.yaxis.set_major_formatter(formatter)
p2 = plt.bar(x, flowsL, 0.35, color='r', bottom=0)
p3 = plt.bar(x + 0.35, flowsT, 0.35, color='g', bottom=0)

plt.xticks(x, ('ODL', 'ONOS', 'Ryu', 'Floodlight'), ha="left")
ax.set_title("24 Switches 500 MACs\nCbench")
ax.legend((p2[0], p3[0]), ('Latency', 'Througput'))
ax.set_ylabel("Flows/Sec")
ax.set_xlabel("SDN Controllers")
ax.autoscale_view()
plt.show()
