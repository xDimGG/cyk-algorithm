import itertools
import cfg

# Parse from grammar.txt
c = cfg.parse_file('grammar.txt')

# Assert that the grammar is in CNF
c.assert_cnf()

# Check if the langauge recognizes s
# Construct CYK table like so
# T_21
# T_11 T_12
# s[0] s[1]

# s should not contain epsilon
s = 'ac'

# T_11 = all variables that generate s[0]
T_11 = c.rule_to_variables([s[0]])

# T_12 = all variables that generate s[1]
T_12 = c.rule_to_variables([s[1]])

# Cross product of T_11 and T_12
product = itertools.product(T_11, T_12)

# T_21 = all variables that generate s
T_21 = set()
for p in product:
	T_21 |= c.rule_to_variables(p)

# Check if the start symbol is in T_21
print(s, 'is in L(G)?', c.S in T_21)
