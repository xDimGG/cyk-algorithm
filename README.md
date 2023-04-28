# cyk-algorithm
CFG (Context-Free Grammar) parser + CYK (Cocke-Younger-Kasami) algorithm to determine whether a string is in the language.
Demonstrate the Cocke-Younger-Kasami (CYK) Algorithm. This rep contains a Python program for reading the languages of context-free grammar (CFG) for context-free languages (CFL). 
Note that, the CFG of the given language must be converted to Chomsky Normal Form (CNF) before being read by the program.

Files:
  cyk.py - Contains the algorithm to check whether a language in Chomsky Normal Form contains a specific string
  cfg.py - Contains helper methods for parsing a grammer into a formatted dictionary of rules and checking if said grammer is in Chomsky Normal Form 
  example.py - A program which parses grammer.txt for an input string and grammer and checks whether the input string is contained in the language
  
Data Structures Used:
	Used a python dictionary to represent the language, with the key being the Variable targeted and the value being an array of different mappings the rule   can lead to
	Used a matrix in the form of nested arrays to represent the cyk algorithm table 
CYK Algorithm Used:
	1 -> Creates a base row with Variables derived from each character using rules
	2 -> Creates rows equaling to length of string - 1 with each row having 1 less column than the last
	3 -> For each row iterates through the columns adding Variables that apply to each combination of cells/rules
	4 -> If final row contains S variable, prints success else prints failure
