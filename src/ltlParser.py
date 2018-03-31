from antlr4 import InputStream

from model.ltl.LTLLexer import LTLLexer, CommonTokenStream
from model.ltl.LTLParser import LTLParser
from src.model.ltl.Formula import Formula


def ltlParse(str_: str) -> Formula:
    inputStream = InputStream(str_)

    lexer = LTLLexer(inputStream)
    tokens = CommonTokenStream(lexer)
    parser = LTLParser(tokens)
    ltl = parser.ltl().f
    return ltl if parser.getNumberOfSyntaxErrors() == 0 else None
