# inverse-problem-chlorine-diff

This is a simple repository for solving an assignment. 

Run on Python 3.8 or superior. Requires numpy, pandas, jupyter and matplotlib.


## Project: Estimation of the chloride diffusivity in concrete sample

For now, I've implemented the Least Square approach to estimate the diffusion coefficient of chlorides and the chloride concentration at the exposed sample surface based on the real-life measurements of the chloride ions. 

The didact version is on the notebook `least_square_ex_notebook.ipynb` A succinct version can be runned directly on the terminal:

`python least_squares.example.py <data_name> <months> <expanssion_terms>`

For example, if you want to calculate the regression for data1, 3 months and 1st term you can input on the terminal:

`python least_squares.example.py data1 3 1`

The data is on the data directory.
The plost are saved on plots directory.
