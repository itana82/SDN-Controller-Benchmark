import pandas as pd
import matplotlib.pyplot as plt

def line_plot(input_file, plot_type, units):
    df = pd.read_csv(input_file)
    print(plot_type)

    # 0 refers to making the 1st colum the x-axis, [1,2,3,4] refers to making columns 1-4 the y axis data
    # The 1st row will be used as labels
    df.plot(0, [1, 2, 3, 4],)
    plt.ylabel(units)
    plt.show()
