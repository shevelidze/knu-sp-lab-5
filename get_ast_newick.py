def get_ast_newick(ast, add_semicolon = True):
    if ast[0] == 'grouped':
        result = f"({get_ast_newick(ast[1], add_semicolon=False)})Parentheses"
    elif ast[0] == 'binop':
        result = f"({get_ast_newick(ast[2], add_semicolon=False)},{get_ast_newick(ast[3], add_semicolon=False)}){ast[1]}"
    elif ast[0] == 'unary':
        result = f"({get_ast_newick(ast[2], add_semicolon=False)}){ast[1]}"
    else:
        result = str(ast[1])

    if add_semicolon:
        result += ';'
    
    return result
