from constraint import Problem, AllDifferentConstraint
from itertools import product

columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
rows = [1, 2, 3, 4, 5, 6, 7, 8]

mapping = dict((x, y) for x, y in zip(columns, rows))

def get_bishop_func(x, y):
    def bishop_func(a, b):
        return abs(mapping[x] - mapping[y]) != abs(a - b)
    return bishop_func

problem = Problem()

problem.addVariables(columns, rows)
problem.addConstraint(AllDifferentConstraint())

for column1, column2 in product(columns, columns):
    if column1 < column2:
        problem.addConstraint(get_bishop_func(column1, column2), (column1, column2))

for solution in problem.getSolutions():
    print sorted(solution.iteritems())


