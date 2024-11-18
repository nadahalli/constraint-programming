from constraint import *

problem = Problem()

root = 3
length = root*root
size = length*length

problem = Problem()
problem.addVariables(range(0, size), range(1, length + 1))
for i in range (length):
    rowDifferentConstraint = [j for j in range(i * length, (i+1)*length)]
    problem.addConstraint(AllDifferentConstraint(), rowDifferentConstraint)
    colDifferentConstraint = [j for j in range(i, size, length)]
    problem.addConstraint(AllDifferentConstraint(), colDifferentConstraint)

for i in range(0, size, root * length):
    for j in range(i, i + length, root):
        innerSquareConstaint = []
        for k in range(root):
            for l in range(root):
                innerSquareConstaint.append(j + (k*length) + l)
        problem.addConstraint(AllDifferentConstraint(), innerSquareConstaint)

def printSolution(solution):
    for i in range(length):
        row = '.'.join([str(solution[i * length + j]) for j in range(0, length)])
        print(row)
    print('-' * 10)

for solution in problem.getSolutionIter():
    printSolution(solution)
                       
    
