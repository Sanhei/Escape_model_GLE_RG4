# Escape_model_GLE_RG4
Kramer's escape time, is a similar problem, with the Generalized Langevin Equation. 

The model is created in model.py.
## Purpose
As a subproject of my master thesis, in this part, we will discuss the model without recrossing, which is known as the escape model or Kramers problem.

## Integrator
The stochastic differential equation model uses Runge-Kutta's fourth order. We validate the model by free energy plotting

![alt text](https://github.com/Sanhei/Escape_model_GLE_RG4/blob/main/potential.svg?raw=true)

and Memory kernel extraction:

![alt text](https://github.com/Sanhei/Escape_model_GLE_RG4/blob/main/memory.svg?raw=true)

# Initial velocity distribution
For the initial velocity distribution, we define the function in v_distribution.py.
The random generator of the characterized distribution uses the Monte Carlo method. 
A simple test example:
![alt text](https://github.com/Sanhei/Escape_model_GLE_RG4/blob/main/test.png?raw=true)
# Usage
Check loop.sh
# For cluster or HPC simulation
The program is designed by the multicore package
```
 multiprocessing.Pool()
```
The parallel core usage won't infect the other program.
For memory usage, it depends on the iterations. For instance, $10^5$, it needs 2GB. 



