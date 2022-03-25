import itertools

import gurobipy as gp
from gurobipy import GRB
import numpy as np

model = gp.Model('HelloWorld')
# # setup other parameters

# model.Params.DisplayInterval = 300
# model.Params.TimeLimit = 10
x = model.addVar(lb = 0, vtype = GRB.CONTINUOUS, name = 'foobar')
y = model.addVar(lb = 0, vtype = GRB.CONTINUOUS)
# lb = lowwer bound (default = 0)
# up = upper bound (default = vô cung)
# GRB.CONTINUOUS : bien lien tuc
# GRB.INTEGER: biến nguyên
# GRB.BINARY: nhị phân

model.addConstr(x + y <= 5)
model.addConstr(4*x + y <= 11)
model.setObjective(2*x+y, sense = GRB.MAXIMIZE) # hàm mục tiêu


model.optimize()
# print('-' * 50)
# if model.status == GRB.OPTIMAL:
#     print('The status meaning is OPTIMAL')
# print(f'model status: {model.status}')
# print(f'model runtime: {model.runtime}')
# # use the syntax foo.x to access the optimal value of foo
# print(f'x: {x.x}')
# print(f'y: {y.x}')


# -------------------------------------------------------------
def getAllCells(n):
    return tuple(itertools.product(range(n), repeat = 2))

def getMajorDiagonalCells(n, diff):
    assert 1 - (n-1) <= diff <= (n-1) - 1
    return [(x, y) for (x, y) in getAllCells(n) if x - y == diff]

def getAntiDiagonalCells(n, total):
    assert 0 + 1 <= total <= (n-1) + (n-2)
    return [(x, y) for (x, y) in getAllCells(n) if x + y == total]
n = 8

env = gp.Env(empty = True)
# env.setParam('OutputFlag', 0)
env.start()
model = gp.Model('QueensInTheChessBoard', env = env)
# model.Params.DisplayInterval = 300
vars = model.addMVar(shape = (n, n), vtype = GRB.BINARY)
model.addConstrs(vars[:, i].sum() <= 1 for i in range(n))
model.addConstrs(vars[i, :].sum() <= 1 for i in range(n))

minDiff, maxDiff = 1 - (n-1), (n-1) - 1
for diff in range(minDiff, maxDiff + 1):
    arr = np.array(getMajorDiagonalCells(n, diff))
    lhs = vars[
        arr[:, 0],
        arr[:, 1],
    ]
    model.addConstr(lhs.sum() <= 1)
    
    minTotal, maxTotal = 0 + 1, (n-1) + (n-2)
for total in range(minTotal, maxTotal + 1):
    arr = np.array(getAntiDiagonalCells(n, total))
    lhs = vars[
        arr[:, 0],
        arr[:, 1],
    ]
    model.addConstr(lhs.sum() <= 1)
    
    # problemB: enumerate all solutions
model.addConstr(vars.sum() == n)
solutionsCounter = 0
while True:
    model.optimize()
    if model.status == GRB.OPTIMAL:
        solutionsCounter += 1
        resultArray = vars.x.astype(int)
        print(resultArray)
        xAxisIndices, yAxisIndices = resultArray.nonzero()
        model.addConstr(vars[xAxisIndices, yAxisIndices].sum() <= n - 1)
    elif model.status == GRB.INFEASIBLE:
        break
    else:
        raise ValueError(f'impossible status {model.status}')
print(f'\nTotal number of solutions: {solutionsCounter}')