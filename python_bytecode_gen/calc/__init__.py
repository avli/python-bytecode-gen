"""Compiles simple expressions to Python bytecode.

To be precise, a "simple expression" is:

    expr : NUMBER ('+'|'-' NUMBER)* NEWLINE;
    NUMBER : '0'..'9'+ ;
    NEWLINE : '\n' ;

"""
from python_bytecode_gen.calc.compiler import Compiler
from python_bytecode_gen.calc.lexer import Lexer
from python_bytecode_gen.calc.parser import Parser


def gencode(source):
    source += '\n'
    lexer = Lexer(source)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    ast = parser.parse()
    compiler = Compiler()
    codeobj = compiler.compile(ast)
    return codeobj
