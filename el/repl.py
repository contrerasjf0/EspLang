from el.lexer import Lexer
from el.token import (
    Token,
    TokenType,
)


EOF_TOKEN: Token = Token(TokenType.EOF, '')


def start_repl() -> None:
    while (source := input('>> ')) != 'salir()':
        lexer: Lexer = Lexer(source)

        while (token := lexer.next_token()) != EOF_TOKEN:
            print(token)

