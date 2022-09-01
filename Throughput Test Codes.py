#MEng Thesis
#Date : 23 August 2022
#Author : Kristof Itana
#Institution : UCT

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set directory
df = pd.read_csv('C:\\Users\kristof.itana\Downloads\Throughput_Results.csv')
print(df.shape)
df.info()


df.plot()
# Set label
plt.xlabel('No.of Switches')
plt.ylabel('Throughput(responses/sec)')
plt.legend()

plt.show()
