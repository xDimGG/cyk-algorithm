from sys import argv
from cfg import parse_file
# from itertools import product
import itertools

assert len(argv) > 2

string = argv[2]

cfg = parse_file(argv[1])
cfg.assert_cnf()

# create the empty matrix
matrix = []

# create the row with reversed order 
for size in range(len(string), 0, -1):
    # each row is a list that can contain multiple sets each corresponding to a cell in the cyk
    row = []
    for i in range(size):
        # create sets for each row since there are no repititions we should use set
        row.append(set())
    matrix.append(row)

# since first row is converted from string we should treat it especially
for i in range(len(string)):
    matrix[0][i] = cfg.rule_to_variables(string[i])

for i in range(1, len(string)):
    for j in range(len(string)-i):
        for k in range(i):
            for rhs in itertools.product(matrix[k][j], matrix[i - 1 - k][j + 1 + k]):
                matrix[i][j] |= cfg.rule_to_variables(rhs)

if cfg.S in matrix[-1][0]: 
    print(f'{string} is in the language')
else:
    print(f'{string} is not in the language')

print(matrix)
