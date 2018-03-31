# Generated from LTL.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LTLParser import LTLParser
else:
    from LTLParser import LTLParser

from src.model.ltl.LTL import LTL


# This class defines a complete listener for a parse tree produced by LTLParser.
class LTLListener(ParseTreeListener):

    # Enter a parse tree produced by LTLParser#ltl.
    def enterLtl(self, ctx:LTLParser.LtlContext):
        pass

    # Exit a parse tree produced by LTLParser#ltl.
    def exitLtl(self, ctx:LTLParser.LtlContext):
        pass


    # Enter a parse tree produced by LTLParser#primary.
    def enterPrimary(self, ctx:LTLParser.PrimaryContext):
        pass

    # Exit a parse tree produced by LTLParser#primary.
    def exitPrimary(self, ctx:LTLParser.PrimaryContext):
        pass


    # Enter a parse tree produced by LTLParser#constant.
    def enterConstant(self, ctx:LTLParser.ConstantContext):
        pass

    # Exit a parse tree produced by LTLParser#constant.
    def exitConstant(self, ctx:LTLParser.ConstantContext):
        pass


