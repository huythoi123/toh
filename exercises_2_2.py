import itertools
from operator import mod

import gurobipy as gp
from gurobipy import GRB
import numpy as np

model = gp.Model()
model.Params.DualReductions = 0
x = model.addVar(lb=0, vtype=GRB.CONTINUOUS)

model.addConstr(x >= 0)
model.setObjective(x, sense=GRB.MAXIMIZE)

model.optimize()
print('-' * 50)
if model.status == GRB.OPTIMAL:
    print('The status meaning is OPTIMAL')
    print(f'x1: {x.x}')
elif model.status == GRB.INFEASIBLE :
    print('the status meaning is INFEASIBLE')
elif model.status == GRB.UNBOUNDED :
    print('the status meaning is UNBOUNDED')
print(f'model status: {model.status}')
print(f'model runtime: {model.runtime}')
# use the syntax foo.x to access the optimal value of foo
