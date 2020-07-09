# OMP Solver
> Solver for the ore mixing problem | Scientific Research

## Ore Mixing or Blending Problem

The ore mixing or blending problem consists in determining the quantity of each ore, coming from a set of fronts or piles, which must be blended to form a final product with characteristics that meet the requirements of a given customer. As the ores have different characteristics, whether the content of a certain chemical element or the percentage of an ore in a certain granulometric range, it is necessary to combine the ores in certain proportions so that the mixture meets the quality and quantity targets.

## Getting Started

The source code includes the linear model and a greedy heuristic for the OMP.

Note that specific input files are required to execute the solver, available at <a href="https://github.com/gabriaraujo/omp/tree/master/tests" target="_blank"> `tests`</a> folder.

To use the solver properly, run the commands from the root directory.

    python3 src/main.py <input argument> <output argument>

    Usage exemple:
    python3 src/main.py instance_1.json out_1.json

The solver outputs can be found in the <a href="https://github.com/gabriaraujo/omp/tree/master/out" target="_blank">`out`</a> folder. The generated results can be found in the <a href="https://github.com/gabriaraujo/omp/tree/master/out/json" target="_blank">`json`</a> subfolder and the model details (lp format) in the <a href="https://github.com/gabriaraujo/omp/tree/master/out/logs" target="_blank">`logs`</a> subfolder. 

## Instance Generator
An instance generator for OMP was also developed.

To use the instance generator properly, run the commands from the root directory.

    python3 src/main.py <json file name> [options]

    Optional parameters (see the note below):
        -name <str>       : internal name for the instance (default: Instance_R{1, ..., 1000}).
        -stockpiles <int> : amount of stockpiles for the problem (default: 4).
        -capacity <float> : capacity of each stockpile (default: 400).
        -outputs <int>    : number of orders to be fulfilled (default: 1).
        -weight <float>   : total ore mass of each order (default: 1000.0).
        -inputs <int>     : amount of ore input to the problem (default: 1).
        -engines <int>    : amount of equipment available (default: 2).
        -variant <float>  : rate of change for quality and quantity of ores (default: 0.2).

    Usage exemple:    	
    python3 src/gen.py instance_1.json Instance_M001 4 600 2 1000 1 2 0.2

Note that for the optional parameters to work as expected they must be entered in the exact order listed above.

## Dependencies
- <a href="https://numpy.org" target= "_blank">NumPy</a> - Library that offers comprehensive mathematical functions, random number generators, linear algebra routines, Fourier transforms, and more.
- <a href="https://pypi.org/project/ujson/" target= "_blank">UltraJSON</a> - Ultra fast JSON encoder and decoder for Python.
- <a href="https://pypi.org/project/mip/" target= "_blank">Python MIP</a> - Python tools for Modeling and Solving Mixed-Integer Linear Programs (MIPs).

## Questions?
If you have any questions, please feel free to contact me.

Thanks!