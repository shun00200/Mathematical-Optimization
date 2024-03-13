import pandas as pd
import pulp
import time

# Read CSV files
customer_df = pd.read_csv('customers.csv')
prob_df = pd.read_csv('visit_probability.csv')

# Set up a linear programming problem
problem = pulp.LpProblem('CustomerSegmentation', pulp.LpMaximize)

# Define decision variables
I = customer_df['customer_id'].to_list()
M = [1, 2, 3]  # Direct mail types
x_im = {(i, m): pulp.LpVariable(f'dm_{i}_{m}', cat='Binary') for i in I for m in M}

# Ensure each customer is assigned to one segment
for i in I:
    problem += pulp.lpSum(x_im[i, m] for m in M) == 1, f"OneSegmentPerCustomer_{i}"

# Merge customer and probability dataframes and reshape
customer_prob_df = pd.merge(customer_df, prob_df, on=['age_cat', 'freq_cat'])
customer_prob_ver_df = customer_prob_df.rename(
    columns={'prob_dm1': 1, 'prob_dm2': 2, 'prob_dm3': 3}
).melt(id_vars=['customer_id'], value_vars=[1, 2, 3], var_name='dm', value_name='prob')

# Convert to dictionary for faster access
P_im = customer_prob_ver_df.set_index(['customer_id', 'dm'])['prob'].to_dict()

# Set the objective function to maximize probability difference
problem.objective += pulp.lpSum((P_im[i, m] - P_im[i, 1]) * x_im[i, m] for i in I for m in [2, 3])

# Set a constraint for the maximum marketing budget
price = {1: 0, 2: 1000, 3: 2000}
problem += pulp.lpSum(P_im[i,m] * x_im[i, m] * price[m] for i in I for m in M) <= 1e6, "BudgetConstraint"

# Ensure a minimum percentage of customers are targeted in each segment
S = prob_df['segment_id'].unique()
N_s = customer_prob_df.groupby('segment_id')['customer_id'].nunique()
s_i = customer_prob_df.set_index('customer_id')['segment_id'].to_dict()
for s in S:
    for m in M:
        problem += pulp.lpSum(x_im[i, m] for i in I if s_i[i] == s) >= 0.1 * N_s[s], f"MinSegmentTarget_{s}_{m}"

# Solve the problem
time_start = time.time()
status = problem.solve()
time_stop = time.time()

# Output the results
print(f'Status: {pulp.LpStatus[status]}')
print(f'Objective Value: {pulp.value(problem.objective):.4f}')
print(f'Execution Time: {(time_stop - time_start):.3f} seconds')
