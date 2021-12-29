from calc.lexer import PLUS, MINUS, NUMBER, Lexer


class AST:
    def accept(self, visitor):
        return visitor.visit(self)


class Expr(AST):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __repr__(self):
        return "<Expr(%s, %s, %s)>" % (self.left, self.op, self.right)


class Number(AST):
    def __init__(self, number):
        self.number = number

    def __repr__(self):
        return "<Number(%s)>" % self.number


class Parser:
    def __init__(self, tokens):
        self._tokens = tokens
        self._current = 0

    def parse(self):
        return self._prog()

    def _prog(self):
        return self._expr()

    def _expr(self):
        expr = self._number()

        while self._match(PLUS, MINUS):
            op = self._advance()
            right = self._number()
            expr = Expr(expr, op, right)

        return expr

    def _number(self):
        if self._match(NUMBER):
            return Number(self._advance())
        raise RuntimeError("Unexpected token %r" % self._peek())

    def _is_at_end(self):
        return self._current <= len(self._tokens)

    def _advance(self):
        self._current += 1
        return self._tokens[self._current - 1]

    def _match(self, *types):
        for type in types:
            if self._peek().type == type:
                return True
        return False

    def _peek(self):
        return self._tokens[self._current]


class Visitor:
    def visit(self, node):
        raise NotImplementedError


class AstPrinter(Visitor):
    def print(self, root):
        print(root.accept(self))

    def visit(self, node):
        if isinstance(node, Number):
            return node.number.literal
        elif isinstance(node, Expr):
            return '(%s %s %s)' % (node.op.lexeme, node.left.accept(self), node.right.accept(self))


class Interpreter(Visitor):
    def interpret(self, root):
        return root.accept(self)

    def visit(self, node):
        if isinstance(node, Number):
            return node.number.literal
        elif isinstance(node, Expr):
            if node.op.type == PLUS:
                return node.left.accept(self) + node.right.accept(self)
            else:
                return node.left.accept(self) - node.right.accept(self)


def main():
    while True:
        source = input('> ')
        source += '\n'
        try:
            lexer = Lexer(source)
            tokens = lexer.tokenize()
            parser = Parser(tokens)
            ast = parser.parse()
            # ast_printer = AstPrinter()
            # ast_printer.print(ast)
            interpreter = Interpreter()
            print(interpreter.interpret(ast))
        except RuntimeError as e:
            print(e)


if __name__ == '__main__':
    main()
