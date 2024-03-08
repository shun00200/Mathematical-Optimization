import pulp

problem = pulp.LpProblem('LP', pulp.LpMaximize)

x = pulp.LpVariable('x', cat='Continuous')
y = pulp.LpVariable('y', cat='Continuous')

problem += 2 * x + 3 * y <= 30
problem += 3 * x + 2 * y <= 50
problem += x >= 0
problem += y >= 0
problem.objective = 2*x + 3*y

status = problem.solve()

print('Status:', pulp.LpStatus[status])
print('x=', x.value(), 'y=', y.value(), 'obj=', problem.objective.value())