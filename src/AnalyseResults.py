# import Plotting
import DataHandling
import argparse

def read_args():
    """Configure what parameters can/should be passed to the script using argparse"""
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--input_file',
                        type=str,
                        required=True,
                        help='Provide the full path to the data input file to be processed'
                        )
    parser.add_argument('-p', '--plot_type',
                        default='line',
                        type=str,
                        help='Provide the type of plot to be generated.  Select from: line, scatter, histogram'
                        )
    parser.add_argument('-u', '--unit',
                        default='unknown',
                        type=str,
                        help='Provide the unit being plotted.  Provided string will be used to lable the graph'
                        )
    args = parser.parse_args()
    return args


def main():
    # Read in parameters for this run of the script
    args = read_args()
    print(args)
    DataHandling.line_plot(args.input_file, args.plot_type, args.unit)

if __name__ == "__main__":
    main()
