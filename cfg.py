from collections import defaultdict

class Grammar:
	EPSILON = 'e'

	def __init__(self, V: set[str], T: set[str], R: dict[str, list[list[str]]], S: str):
		"""
		V:   variables
		T:   terminals
		R:   rules (map from variable to rules)
		S:   start symbol

		Example of R:
		if we have the following rules:
		S -> aS | bA
		A -> AA | b | e
		the corresponding R would be the following dict
		{
			'S': [['a', 'S'], ['b', 'A']],
			'A': [['A', 'A'], ['b'], ['e']],
		}
		"""
		# epsilon is reserved
		assert self.EPSILON not in T

		# V and T must be disjoint
		assert V.isdisjoint(T)

		# S must be a variable 
		assert S in V

		# S must have a defined rule
		assert S in R and len(R[S]) > 0

		# All symbols
		all_symbols = V | T | {self.EPSILON}

		for a, rules in R.items():
			# Left side must be a variable
			assert a in V

			# Assert all the rules are valid (a -> b)
			for b in rules:
				# Right side should not be empty
				assert len(b) > 0

				# Right sides items must be a variable, terminal, or epsilon
				for s in b:
					assert s in all_symbols

		self.V = V
		self.T = T
		self.R = R
		self.S = S

		# pre-compute rule to variables for O(1) lookup
		# tuples are used because they are immutable
		self._rule_to_variables = defaultdict(set)
		for a, rules in R.items():
			for b in rules:
				self._rule_to_variables[tuple(x for x in b if x != self.EPSILON)] |= {a}
	
	def assert_cnf(self):
		"""
		Asserts the grammar is in Chomsky Normal Form
		Does not return anything
		"""
		# Non-start variables
		non_start = self.V - {self.S}

		for a, rules in self.R.items():
			for b in rules:
				# |b| < 3
				assert len(b) < 3
				# if |b| == 0 then a must be the start symbol
				if len(b) == 1 and b[0] == self.EPSILON:
					assert a == self.S
				# if |b| == 1 then b must be a terminal
				elif len(b) == 1:
					assert b[0] in self.T
				# if |b| == 2 then both symbols must be non-start variables
				elif len(b) == 2:
					assert b[0] in non_start and b[1] in non_start

	def rule_to_variables(self, B: list[str]) -> set[str]:
		"""
		Returns all A that satisfy A->B
		Filters out any epsilon symbols from B
		"""
		return self._rule_to_variables[tuple(x for x in B if x != self.EPSILON)]

# A->B
RULE_AB_SEPARATOR = '->'
# x->B|C|D|...
RULE_OR_SEPARATOR = '|'

def parse_lines(lines: list[str]) -> Grammar:
	"""
	first line: variables
	second line: terminal symbols
	remaining lines: rules of the form V->AbCd|c|e|...
	note: the first rule's left symbol is used as the start symbol
	"""
	V = set(lines[0])
	T = set(lines[1])

	R = defaultdict(list)
	S = None
	for line in lines[2:]:
		# Skip empty lines
		if line == '':
			continue

		a, b = line.split(RULE_AB_SEPARATOR, 1)
		if S is None:
			S = a

		R[a] += [list(r) for r in b.split('|')]

	return Grammar(V, T, dict(R), S)

def parse_file(file: str) -> Grammar:
	return parse_lines([l.strip() for l in open(file, encoding='utf-8').readlines()])
