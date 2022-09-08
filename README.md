# SDN Controller Benchmarking
The following repository contains both code for benchmarking 4 different SND controllers and analysising the results.  The following README is broken into 2 sections, the first describing how to run the benchmarks and the second on how to plot the results.  Finally, notes on how to contribute to this project and its licensing are given at the end.
* [Running the benchmarks](#running-the-benchmarks)
* [Analysing the results](#analysing-the-results)
* [Contributing and License](#contributing)

## Running the benchmarks

## Analysing the results

### Dependancies
* python3
* pandas
* matplotlib

### How to Use
```bash```
git clone https://github.com/r4space/SDN-Controller-Benchmark.git
cd SDN-Controller-Benchmark/src
python3 AnalyseResults.py -f ../example_data/Latency_Results.csv -u Latency\ \(ms\) -p bar
```bash```

#### Help
To see all script options run help:
```bash```
python3 AnalyseResults.py --help
```bash```


### How to develop
This repo includes a definition of the python environment required using poetry.  

## Contributing
To contribute to this project read the above guides on how to use and develop the code.  
* To report a bug or error pleases raise an issue on Github
* To improve the code base please fork the repository and submit a pull request

### LICENSE:
This repository is licensed under <???> which can be found <here>
