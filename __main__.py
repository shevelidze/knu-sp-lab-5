from ete3 import Tree

from yacc_lex import parser
from executor import Executor
from get_ast_newick import get_ast_newick

expression_string = input('Enter a mathematical expression: ')

if (len(expression_string) == 0):
    expression_string = '2 * ((4 + (7 * 5))/3) - ((9/2) - (8/4)) * ((6 * (3 + 5))/2)'
    print(f'Using a predefined test expression: {expression_string}')

ast = parser.parse(expression_string)
executor = Executor(ast)

ete_tree = Tree(get_ast_newick(ast), format=1)

print('Execution result:', executor.execute()[1])
print('ASCII tree representation: ', ete_tree.get_ascii())

ete_tree.show()



