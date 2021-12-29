from opcode import opmap
from types import CodeType

from calc.lexer import PLUS
from calc.parser import Number, Visitor, Expr


class Compiler(Visitor):
    def __init__(self):
        self._bytecode = []
        self._consts = []
        self._stacksize = self._maxstacksize = 0

    def compile(self, root):
        root.accept(self)
        self._bytecode.append(opmap['RETURN_VALUE'])
        return CodeType(
            0,  # argcount
            0,  # posonlyargcount
            0,  # kwonlyargcount
            0,  # nlocals
            self._maxstacksize,  # stacksize
            64,  # flags (?)
            bytes(self._bytecode),  # codestring
            tuple(self._consts),  # constants
            (),  # names
            (),  # varnames
            "<string>",  # filename
            "",
            1,  # firstlineno
            bytes([len(self._bytecode), 1]),  # lnotab
            (),  # freevars
            (),  # cellvars
        )

    def visit(self, node):
        if isinstance(node, Number):
            self._bytecode.append(opmap['LOAD_CONST'])
            if node.number.literal not in self._consts:
                self._consts.append(node.number.literal)
                index = len(self._consts) - 1
            else:
                index = self._consts.index(node.number.literal)
            self._bytecode.append(index)
            self._stacksize += 1
            self._maxstacksize = max(self._maxstacksize, self._stacksize)

        elif isinstance(node, Expr):
            node.left.accept(self)
            node.right.accept(self)
            if node.op.type == PLUS:
                self._bytecode.append(opmap['BINARY_ADD'])
            else:
                self._bytecode.append(opmap['BINARY_SUBTRACT'])
            self._bytecode.append(0)
            self._stacksize -= 1
