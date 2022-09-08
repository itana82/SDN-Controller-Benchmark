import pandas as pd
import matplotlib.pyplot as plt


def simple_plots(input_file, plot_type, units):
    """
    Makes basic plots from input csv files containing performance metrics of various SDN Controllers versus the number of switches used (first column)
    @param input_file: String of the relative path to the input csv file
    @param plot_type: String indicating the type of plot desired: line, bar, or barh
    @param units: String of the units to annotate the y axis with.
    """
    df = pd.read_csv(input_file)

    if plot_type == 'line':
        df.plot(0, ylabel=units, kind=plot_type, marker="o")
    else:
        df.plot(0, ylabel=units, kind=plot_type)

    plt.show()
