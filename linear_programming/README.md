# Linear Programming Problem Solutions

This repository contains solutions to a specific linear programming problem implemented using two different approaches: a naive brute force algorithm and the PuLP library in Python.

## Naive Brute Force Algorithm

The first approach is a naive brute force solution to the linear programming problem. This method involves systematically enumerating all possible candidate solutions and checking whether each candidate satisfies the problem's constraints. While this approach is straightforward and easy to understand, it is not efficient for larger problems due to its exponential time complexity.

The brute force algorithm is implemented in `brute_force_solution.py`. This script demonstrates how the algorithm searches through the entire solution space to find the optimal solution, albeit inefficiently.

## PuLP Solution

The second approach utilizes PuLP, a popular linear programming library in Python, to solve the same problem more efficiently. PuLP provides a high-level interface for defining problems and calling underlying solvers, which makes it much easier and faster to find optimal solutions for linear programming problems.

The PuLP solution is implemented in `pulp_solution.py`. This script shows how to define the problem constraints and objective function in PuLP, and how to solve the problem using one of the available solvers in the library

## Example of Coupon Distribution

### Objective
- Distribute discount coupons to members to maximize their number of store visits while staying within a budget.

### Details
- Determine which direct mail pattern to send to each member.
- Only one direct mail pattern can be sent to each member.
- Maximize the increase in customer visits due to coupon distribution.
- Total expected budget consumption by members should not exceed 1 million yen.
- Ensure each direct mail pattern is sent to at least 10% of the members in each segment.

### Execution Results
![Figure 1](https://github.com/shun00200/Mathematical-Optimization/blob/images/images/figure1.png)



### Measures
- 
