# Generated from Buchi.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from src.model.buchi.State import State
from src.model.buchi.Transition import Transition
from src.model.ltl.LTL import LTL


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\27")
        buf.write("\177\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write("\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4")
        buf.write("\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7")
        buf.write("\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\7\24m\n")
        buf.write("\24\f\24\16\24p\13\24\3\24\3\24\3\24\3\24\3\24\3\25\3")
        buf.write("\25\7\25y\n\25\f\25\16\25|\13\25\3\26\3\26\3n\2\27\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27\3\2\5\5\2")
        buf.write("\13\f\16\17\"\"\4\2C\\c|\6\2\62;C\\aac|\2\u0080\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write("\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2")
        buf.write("\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2")
        buf.write("\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\3-\3\2\2\2\5\63")
        buf.write("\3\2\2\2\7\65\3\2\2\2\t\67\3\2\2\2\139\3\2\2\2\r>\3\2")
        buf.write("\2\2\17A\3\2\2\2\21D\3\2\2\2\23F\3\2\2\2\25I\3\2\2\2\27")
        buf.write("L\3\2\2\2\31Q\3\2\2\2\33S\3\2\2\2\35U\3\2\2\2\37W\3\2")
        buf.write("\2\2!Z\3\2\2\2#]\3\2\2\2%d\3\2\2\2\'h\3\2\2\2)v\3\2\2")
        buf.write("\2+}\3\2\2\2-.\7p\2\2./\7g\2\2/\60\7x\2\2\60\61\7g\2\2")
        buf.write("\61\62\7t\2\2\62\4\3\2\2\2\63\64\7}\2\2\64\6\3\2\2\2\65")
        buf.write("\66\7\177\2\2\66\b\3\2\2\2\678\7<\2\28\n\3\2\2\29:\7u")
        buf.write("\2\2:;\7m\2\2;<\7k\2\2<=\7r\2\2=\f\3\2\2\2>?\7k\2\2?@")
        buf.write("\7h\2\2@\16\3\2\2\2AB\7h\2\2BC\7k\2\2C\20\3\2\2\2DE\7")
        buf.write("=\2\2E\22\3\2\2\2FG\7<\2\2GH\7<\2\2H\24\3\2\2\2IJ\7/\2")
        buf.write("\2JK\7@\2\2K\26\3\2\2\2LM\7i\2\2MN\7q\2\2NO\7v\2\2OP\7")
        buf.write("q\2\2P\30\3\2\2\2QR\7*\2\2R\32\3\2\2\2ST\7+\2\2T\34\3")
        buf.write("\2\2\2UV\7#\2\2V\36\3\2\2\2WX\7(\2\2XY\7(\2\2Y \3\2\2")
        buf.write("\2Z[\7~\2\2[\\\7~\2\2\\\"\3\2\2\2]^\7h\2\2^_\7c\2\2_`")
        buf.write("\7n\2\2`a\7u\2\2ab\7g\2\2bc\7=\2\2c$\3\2\2\2de\t\2\2\2")
        buf.write("ef\3\2\2\2fg\b\23\2\2g&\3\2\2\2hi\7\61\2\2ij\7,\2\2jn")
        buf.write("\3\2\2\2km\13\2\2\2lk\3\2\2\2mp\3\2\2\2no\3\2\2\2nl\3")
        buf.write("\2\2\2oq\3\2\2\2pn\3\2\2\2qr\7,\2\2rs\7\61\2\2st\3\2\2")
        buf.write("\2tu\b\24\2\2u(\3\2\2\2vz\t\3\2\2wy\t\4\2\2xw\3\2\2\2")
        buf.write("y|\3\2\2\2zx\3\2\2\2z{\3\2\2\2{*\3\2\2\2|z\3\2\2\2}~\7")
        buf.write("\63\2\2~,\3\2\2\2\5\2nz\3\b\2\2")
        return buf.getvalue()


class BuchiLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    WS = 18
    BlockComment = 19
    StringLiteral = 20
    Unit = 21

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'never'", "'{'", "'}'", "':'", "'skip'", "'if'", "'fi'", "';'", 
            "'::'", "'->'", "'goto'", "'('", "')'", "'!'", "'&&'", "'||'", 
            "'false;'", "'1'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "BlockComment", "StringLiteral", "Unit" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "WS", "BlockComment", "StringLiteral", 
                  "Unit" ]

    grammarFileName = "Buchi.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


