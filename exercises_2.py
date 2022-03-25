import itertools
from operator import mod

import gurobipy as gp
from gurobipy import GRB
import numpy as np

model = gp.Model( DualReductions = 0)
# model.Params.DualReductions = 0
x1 = model.addVar(lb=2, vtype=GRB.CONTINUOUS)
x2 = model.addVar(lb=0, vtype=GRB.CONTINUOUS)
x3 = model.addVar(lb=0, vtype=GRB.CONTINUOUS)

model.addConstr(x1 <= 1)
model.addConstr(x2 <= 5)
model.addConstr(x3 <= 2)
model.addConstr(4*x1 + x2 + 4*x3 <= 25)
model.setObjective(2*x1 + x2 + 2*x3, sense=GRB.MAXIMIZE)

model.optimize()
print('-' * 50)
if model.status == GRB.OPTIMAL:
    print('The status meaning is OPTIMAL')
    print(f'x1: {x1.x}')
    print(f'x2: {x2.x}')
    print(f'x3: {x3.x}')
elif model.status == GRB.INFEASIBLE :
    print('the status meaning is INFEASIBLE')
elif model.status == GRB.UNBOUNDED :
    print('the status meaning is UNBOUNDED')
print(f'model status: {model.status}')
print(f'model runtime: {model.runtime}')
# use the syntax foo.x to access the optimal value of foo
