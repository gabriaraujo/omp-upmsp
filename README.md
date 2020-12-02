# OMP-UPMSP Solver
> Solver for the Ore Mixing Problem (OMP) and the Unrelated Parallel Machine Schedule Problem (UPMSP).

## 📑 About this Project
This is a research project in Optimization Models and Algorithms in Industry 4.0 and aims to propose heuristic solutions and modeling in linear programming for the [Ore Mixing 
Problem (OMP)](https://github.com/gabriaraujo/omp-upmsp#%EF%B8%8F-ore-mixing-or-blending-problem) and the 
[Unrelated Parallel Machine Schedule Problem (UPMSP)](https://github.com/gabriaraujo/omp-upmsp#-unrelated-parallel-machine-schedule-problem). The ore mixing and blending problem 
consists in determining the quantity of each ore, coming from a 
set of fronts or piles, which must be blended to form a final product with characteristics that meet the requirements of a specific customer. As the ores have different 
characteristics, whether the content of a certain chemical element or the percentage of an ore in a certain granulometric range, it is necessary to combine the ores in certain 
proportions so that the mixture meets the quality and quantity goals. Likewise, the machinery performs the stacking and recovery of materials from the ore stacks and due to the 
load differences between orders and the need to combine the ores to meet the quality standards, the time and the energy required to stack and recover vary considerably by job.

## ⛰️ Ore Mixing or Blending Problem
The ore mixing or blending problem consists in determining the quantity of each ore, coming from a set of fronts or piles, which must be blended to form a final product with characteristics that meet the requirements of a given customer. As the ores have different characteristics, whether the content of a certain chemical element or the percentage of an ore in a certain granulometric range, it is necessary to combine the ores in certain proportions so that the mixture meets the quality and quantity targets.

## 🚜 Unrelated Parallel Machine Schedule Problem
The problem is to schedule a set of jobs, each available at a certain time, on unrelated machines. In this scenario, the machinery performs the stacking and recovery of 
materials from the ore stacks and due to the load differences between orders and the need to combine the ores to meet the quality standards, the time and the energy required 
to stack and recover change considerably by work.

## 💡 Why?
This project is part of my scientific research and I would be very happy to receive feedback on the project, code, structure, anything that can make me a better developer!

E-mail: <a href="mailto:gabrielcaetanodm@gmail.com">gabrielcaetanodm@gmail.com</a> | 
LinkedIn: <a href="https://www.linkedin.com/in/gabrielcaetanodm/" target="_blank">gabrielcaetanodm</a>

The orientations and ideas for this project are provide by [Túlio Toffolo](https://github.com/tuliotoffolo).

## 📥 How to use
- Clone this repository: `git clone https://github.com/gabriaraujo/omp-upmsp.git`

To use just follow the instructions below:

    Usage: python3 src/main.py <input> <output> [options]
    <input>  : Name of the problem input file.
    <output> : Name of the (output) solution file.

    Options:
        -constructive <constructive> : premodel, postmodel (default: postmodel).
        -algorithm <algorithm>       : lahc, sa.
        -feedback <feedback>         : maximum number of feedback interactions with the model (defaulf: 0).
        -seed <seed>                 : random seed (default: 0).
        -maxiters <maxiters>         : maximum number of interactions (default: 1000).

    LAHC parameters:
        -lsize <lsize> : LAHC list size (default: 1000).

    SA parameters:
        -alpha <alpha> : cooling rate for the Simulated Annealing (default: 0.9).
        -samax <samax> : iterations before updating the temperature for Simulated Annealing (default: 1000).
        -t0 <t0>       : initial temperature for the Simulated Annealing (default: 1.0). 

    Examples:
        python3 src/main.py instance_1.json out_1.json
        python3 src/main.py instance_1.json out_1.json -constructive premodel -seed 1
        python3 src/main.py instance_1.json out_1.json -algorithm sa -alpha 0.98 -samax 1000 -t0 1e5
        
Note that specific input files are required to execute the solver, available at <a href="https://github.com/gabriaraujo/omp/tree/master/tests" target="_blank"> `tests`</a> folder. To use the solver properly, run the commands from the root directory.

The solver outputs can be found in the created `out` folder. The generated results can be found in the `json` subfolder and the model details (lp format) in the `logs` subfolder. 

## 💽 Dependencies
- <a href="https://numpy.org" target= "_blank">NumPy</a> - Library that offers comprehensive mathematical functions, random number generators, linear algebra routines, Fourier transforms, and more.
- <a href="https://pypi.org/project/ujson/" target= "_blank">UltraJSON</a> - Ultra fast JSON encoder and decoder for Python.
- <a href="https://pypi.org/project/mip/" target= "_blank">Python MIP</a> - Python tools for Modeling and Solving Mixed-Integer Linear Programs (MIPs).

## 📕 License
The software is available under the Eclipse Public License 2.0](https://github.com/gabriaraujo/omp-upmsp/blob/master/LICENSE).

## ☕ Questions?
If you have any questions, please feel free to contact me.

Thanks!
