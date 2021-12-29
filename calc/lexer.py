class Token:
    def __init__(self, type, lexeme, literal=None):
        self.type = type
        self.lexeme = lexeme
        self.literal = literal

    def __repr__(self):
        return '<Token(%s, %s, %s)>' % (self.type, self.lexeme, self.literal)


# Token types
PLUS = 0
MINUS = 1
NUMBER = 2
NEWLINE = 3


class Lexer:
    def __init__(self, source):
        self._source = source
        self._tokens = []
        self._current = 0
        self._start = 0

    def tokenize(self):
        while not self._is_at_end():
            self._start = self._current
            c = self._advance()
            if c == '+':
                self._tokens.append(Token(PLUS, c))
            elif c == '-':
                self._tokens.append(Token(MINUS, c))
            elif c == '\n':
                self._tokens.append(Token(NEWLINE, '\\n'))
            elif self._is_digit(c):
                self._digit()
            elif self._is_whitespace(c):
                continue
            else:
                raise RuntimeError("Unexpected character at position %d" % self._current)
        return self._tokens

    def _is_at_end(self):
        return self._current >= len(self._source)

    def _advance(self):
        self._current += 1
        return self._source[self._current - 1]

    def _is_digit(self, c):
        return c in '0123456789'

    def _digit(self):
        while self._is_digit(self._peek()):
            self._advance()
        lexeme = self._source[self._start:self._current]
        self._tokens.append(Token(NUMBER, lexeme, int(lexeme)))

    def _peek(self):
        if self._is_at_end():
            return '\0'
        return self._source[self._current]

    def _is_whitespace(self, c):
        return c in ' \t\r'
