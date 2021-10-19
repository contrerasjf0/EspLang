from unittest import TestCase

from el.ast import (
    Identifier,
    LetStatement,
    Program,
    ReturnStatement,
)
from el.token import (
    Token,
    TokenType,
)


class ASTTest(TestCase):

    def test_let_statement(self) -> None:
        let_statement_x = LetStatement(
                token=Token(TokenType.LET, literal='variable'),
                name=Identifier(
                    token=Token(TokenType.IDENT, literal='x'),
                    value='x'
                ),
                value=Identifier(
                    token=Token(TokenType.IDENT, literal='x2'),
                    value='x2'
                )
            )

        program: Program = Program(statements=[
            let_statement_x,
        ])

        program_str = str(program)

        self.assertEquals(program_str, 'variable x = x2')

    def test_return_statement(self) -> None:
        return_statement_x = ReturnStatement(
                token=Token(TokenType.RETURN, literal='regresa'),
                return_value=Identifier(
                    token=Token(TokenType.IDENT, literal='x'),
                    value='x'
                )
            )
        program: Program = Program(statements=[
            return_statement_x,
        ])

        program_str = str(program)

        self.assertEquals(program_str, 'regresa x;')