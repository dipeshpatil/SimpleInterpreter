from Lexer.tokens import TokenType, Token

WHITESPACE = ' \n\t'
DIGITS = '0123456789'


class Lexer:
    def __init__(self, text):
        self.current_char = None
        self.text = iter(text)
        self.advance()

    def advance(self):
        try:
            self.current_char = next(self.text)
        except StopIteration:
            self.current_char = None

    def generate_tokens(self):
        while self.current_char is not None:
            if self.current_char in WHITESPACE:
                self.advance()
            elif self.current_char == '.' or self.current_char in DIGITS:
                yield self.generate_number()

            elif self.current_char == '+':
                self.advance()
                yield Token(TokenType.PLUS)

            elif self.current_char == '-':
                self.advance()
                yield Token(TokenType.MINUS)

            elif self.current_char == '*':
                self.advance()
                if self.current_char == '*':
                    self.advance()
                    yield Token(TokenType.POW)
                else:
                    yield Token(TokenType.MULTIPLY)

            elif self.current_char == '/':
                self.advance()
                if self.current_char == '/':
                    self.advance()
                    yield Token(TokenType.INT_DIVIDE)
                else:
                    yield Token(TokenType.DIVIDE)

            elif self.current_char == '%':
                self.advance()
                yield Token(TokenType.MOD)

            elif self.current_char == '#':
                self.advance()
                yield Token(TokenType.NRT)

            elif self.current_char == 'L':
                char = self.current_char
                self.advance()
                if self.current_char == "B":
                    self.advance()
                    yield Token(TokenType.LOGNBASEX)
                elif self.current_char == "N":
                    self.advance()
                    yield Token(TokenType.NAT_LOG)
                else:
                    raise Exception(f"Illegal Character '{char}'")

            elif self.current_char == "S":
                self.advance()
                if self.current_char == "I":
                    self.advance()
                    yield Token(TokenType.SIN_INV)
                else:
                    yield Token(TokenType.SIN)

            elif self.current_char == "C":
                self.advance()
                if self.current_char == "I":
                    self.advance()
                    yield Token(TokenType.COS_INV)
                else:
                    yield Token(TokenType.COS)

            elif self.current_char == "T":
                self.advance()
                if self.current_char == "I":
                    self.advance()
                    yield Token(TokenType.TAN_INV)
                else:
                    yield Token(TokenType.TAN)

            elif self.current_char == '(':
                self.advance()
                yield Token(TokenType.LPAREN)

            elif self.current_char == ')':
                self.advance()
                yield Token(TokenType.RPAREN)

            else:
                raise Exception(f"Illegal Character '{self.current_char}'")

    def generate_number(self):
        decimal_point_count = 0
        number_str = self.current_char
        self.advance()

        while self.current_char is not None and (self.current_char == '.' or self.current_char in DIGITS):
            if self.current_char == '.':
                decimal_point_count += 1
                if decimal_point_count > 1:
                    break

            number_str += self.current_char
            self.advance()

        if number_str.startswith('.'):
            number_str = '0' + number_str
        if number_str.endswith('.'):
            number_str += '0'

        return Token(TokenType.NUMBER, float(number_str))
