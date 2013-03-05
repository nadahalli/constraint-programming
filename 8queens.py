from constraint import Problem, AllDifferentConstraint
from itertools import product
from functools import partial

columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
rows = [1, 2, 3, 4, 5, 6, 7, 8]

mapping = dict((x, y) for x, y in zip(columns, rows))

def bishop_func(a, b, x, y): return abs(mapping[x] - mapping[y]) != abs(a - b) or a == b

problem = Problem()

problem.addVariables(columns, rows)
problem.addConstraint(AllDifferentConstraint())

for column1, column2 in product(columns, columns):
    problem.addConstraint(partial(bishop_func, x = column1, y = column2), (column1, column2))

for solution in problem.getSolutions():
    print sorted(solution.iteritems())


