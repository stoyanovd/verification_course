# Generated from LTL.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from src.model.ltl.LTL import LTL


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\23")
        buf.write("p\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\6\3\6\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\17\3\17\3\20\3\20\5\20T\n\20\3\21\3\21\3\21\6")
        buf.write("\21Y\n\21\r\21\16\21Z\3\21\3\21\3\22\3\22\3\22\6\22b\n")
        buf.write("\22\r\22\16\22c\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\2\2\26\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\2#\2%\2\'")
        buf.write("\22)\23\3\2\6\6\2\f\f\17\17))^^\6\2\f\f\17\17$$^^\13\2")
        buf.write("$$))^^cdhhppttvvxx\5\2\13\f\16\17\"\"\2q\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2")
        buf.write("\2\2\37\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\3+\3\2\2\2\5-\3")
        buf.write("\2\2\2\7/\3\2\2\2\t\61\3\2\2\2\13\64\3\2\2\2\r8\3\2\2")
        buf.write("\2\17:\3\2\2\2\21<\3\2\2\2\23>\3\2\2\2\25@\3\2\2\2\27")
        buf.write("B\3\2\2\2\31G\3\2\2\2\33M\3\2\2\2\35O\3\2\2\2\37S\3\2")
        buf.write("\2\2!U\3\2\2\2#^\3\2\2\2%g\3\2\2\2\'j\3\2\2\2)n\3\2\2")
        buf.write("\2+,\7~\2\2,\4\3\2\2\2-.\7(\2\2.\6\3\2\2\2/\60\7#\2\2")
        buf.write("\60\b\3\2\2\2\61\62\7/\2\2\62\63\7@\2\2\63\n\3\2\2\2\64")
        buf.write("\65\7>\2\2\65\66\7/\2\2\66\67\7@\2\2\67\f\3\2\2\289\7")
        buf.write("W\2\29\16\3\2\2\2:;\7T\2\2;\20\3\2\2\2<=\7Z\2\2=\22\3")
        buf.write("\2\2\2>?\7I\2\2?\24\3\2\2\2@A\7H\2\2A\26\3\2\2\2BC\7v")
        buf.write("\2\2CD\7t\2\2DE\7w\2\2EF\7g\2\2F\30\3\2\2\2GH\7h\2\2H")
        buf.write("I\7c\2\2IJ\7n\2\2JK\7u\2\2KL\7g\2\2L\32\3\2\2\2MN\7*\2")
        buf.write("\2N\34\3\2\2\2OP\7+\2\2P\36\3\2\2\2QT\5!\21\2RT\5#\22")
        buf.write("\2SQ\3\2\2\2SR\3\2\2\2T \3\2\2\2UX\7)\2\2VY\n\2\2\2WY")
        buf.write("\5%\23\2XV\3\2\2\2XW\3\2\2\2YZ\3\2\2\2ZX\3\2\2\2Z[\3\2")
        buf.write("\2\2[\\\3\2\2\2\\]\7)\2\2]\"\3\2\2\2^a\7$\2\2_b\n\3\2")
        buf.write("\2`b\5%\23\2a_\3\2\2\2a`\3\2\2\2bc\3\2\2\2ca\3\2\2\2c")
        buf.write("d\3\2\2\2de\3\2\2\2ef\7$\2\2f$\3\2\2\2gh\7^\2\2hi\t\4")
        buf.write("\2\2i&\3\2\2\2jk\t\5\2\2kl\3\2\2\2lm\b\24\2\2m(\3\2\2")
        buf.write("\2no\13\2\2\2o*\3\2\2\2\b\2SXZac\3\b\2\2")
        return buf.getvalue()


class LTLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    DIS = 1
    CON = 2
    NOT = 3
    IMPL = 4
    EQ = 5
    UNTIL = 6
    RELEASE = 7
    NEXT = 8
    GLOB = 9
    FUTURE = 10
    TRUE = 11
    FALSE = 12
    LP = 13
    RP = 14
    StringLiteral = 15
    WS = 16
    ErrorChar = 17

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'|'", "'&'", "'!'", "'->'", "'<->'", "'U'", "'R'", "'X'", "'G'", 
            "'F'", "'true'", "'false'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "DIS", "CON", "NOT", "IMPL", "EQ", "UNTIL", "RELEASE", "NEXT", 
            "GLOB", "FUTURE", "TRUE", "FALSE", "LP", "RP", "StringLiteral", 
            "WS", "ErrorChar" ]

    ruleNames = [ "DIS", "CON", "NOT", "IMPL", "EQ", "UNTIL", "RELEASE", 
                  "NEXT", "GLOB", "FUTURE", "TRUE", "FALSE", "LP", "RP", 
                  "StringLiteral", "SingleQuoteSeq", "DoubleQuoteSeq", "EscapeSeq", 
                  "WS", "ErrorChar" ]

    grammarFileName = "LTL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


