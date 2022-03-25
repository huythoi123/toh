import itertools
from operator import mod

import gurobipy as gp
from gurobipy import GRB
import numpy as np

model = gp.Model()

x_1 = model.addVar(lb=0, vtype=GRB.CONTINUOUS)
x_2 = model.addVar(lb=0, vtype=GRB.CONTINUOUS)
x_3 = model.addVar(lb=0, vtype=GRB.CONTINUOUS)

model.addConstr(x_1 <= 4)
model.addConstr(x_2 <= 5)
model.addConstr(x_3 <= 2)
model.addConstr(4*x_1 + x_2 + 4*x_3 <= 25)
model.setObjective(2*x_1 + x_2 + 2*x_3, sense=GRB.MAXIMIZE)

model.optimize()
print('-' * 50)
if model.status == GRB.OPTIMAL:
    print('The status meaning is OPTIMAL')
print(f'model status: {model.status}')
print(f'model runtime: {model.runtime}')
# use the syntax foo.x to access the optimal value of foo
print(f'x_1: {x_1.x}')
print(f'x_2: {x_2.x}')
print(f'x_3: {x_3.x}')
