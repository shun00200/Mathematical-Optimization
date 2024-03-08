# Linear Programming Problem Solutions

This repository contains solutions to a specific linear programming problem implemented using two different approaches: a naive brute force algorithm and the PuLP library in Python.

## Naive Brute Force Algorithm

The first approach is a naive brute force solution to the linear programming problem. This method involves systematically enumerating all possible candidate solutions and checking whether each candidate satisfies the problem's constraints. While this approach is straightforward and easy to understand, it is not efficient for larger problems due to its exponential time complexity.

The brute force algorithm is implemented in `brute_force_solution.py`. This script demonstrates how the algorithm searches through the entire solution space to find the optimal solution, albeit inefficiently.

## PuLP Solution

The second approach utilizes PuLP, a popular linear programming library in Python, to solve the same problem more efficiently. PuLP provides a high-level interface for defining problems and calling underlying solvers, which makes it much easier and faster to find optimal solutions for linear programming problems.

The PuLP solution is implemented in `pulp_solution.py`. This script shows how to define the problem constraints and objective function in PuLP, and how to solve the problem using one of the available solvers in the library.
