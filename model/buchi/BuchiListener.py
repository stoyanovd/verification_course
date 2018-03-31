# Generated from Buchi.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BuchiParser import BuchiParser
else:
    from BuchiParser import BuchiParser

from src.model.buchi.State import State
from src.model.buchi.Transition import Transition
from src.model.ltl.LTL import LTL


# This class defines a complete listener for a parse tree produced by BuchiParser.
class BuchiListener(ParseTreeListener):

    # Enter a parse tree produced by BuchiParser#compilationUnit.
    def enterCompilationUnit(self, ctx:BuchiParser.CompilationUnitContext):
        pass

    # Exit a parse tree produced by BuchiParser#compilationUnit.
    def exitCompilationUnit(self, ctx:BuchiParser.CompilationUnitContext):
        pass


    # Enter a parse tree produced by BuchiParser#stateDefinition.
    def enterStateDefinition(self, ctx:BuchiParser.StateDefinitionContext):
        pass

    # Exit a parse tree produced by BuchiParser#stateDefinition.
    def exitStateDefinition(self, ctx:BuchiParser.StateDefinitionContext):
        pass


    # Enter a parse tree produced by BuchiParser#stateName.
    def enterStateName(self, ctx:BuchiParser.StateNameContext):
        pass

    # Exit a parse tree produced by BuchiParser#stateName.
    def exitStateName(self, ctx:BuchiParser.StateNameContext):
        pass


    # Enter a parse tree produced by BuchiParser#transition.
    def enterTransition(self, ctx:BuchiParser.TransitionContext):
        pass

    # Exit a parse tree produced by BuchiParser#transition.
    def exitTransition(self, ctx:BuchiParser.TransitionContext):
        pass


    # Enter a parse tree produced by BuchiParser#expression.
    def enterExpression(self, ctx:BuchiParser.ExpressionContext):
        pass

    # Exit a parse tree produced by BuchiParser#expression.
    def exitExpression(self, ctx:BuchiParser.ExpressionContext):
        pass


    # Enter a parse tree produced by BuchiParser#empty.
    def enterEmpty(self, ctx:BuchiParser.EmptyContext):
        pass

    # Exit a parse tree produced by BuchiParser#empty.
    def exitEmpty(self, ctx:BuchiParser.EmptyContext):
        pass


    # Enter a parse tree produced by BuchiParser#unit.
    def enterUnit(self, ctx:BuchiParser.UnitContext):
        pass

    # Exit a parse tree produced by BuchiParser#unit.
    def exitUnit(self, ctx:BuchiParser.UnitContext):
        pass


    # Enter a parse tree produced by BuchiParser#literal.
    def enterLiteral(self, ctx:BuchiParser.LiteralContext):
        pass

    # Exit a parse tree produced by BuchiParser#literal.
    def exitLiteral(self, ctx:BuchiParser.LiteralContext):
        pass


    # Enter a parse tree produced by BuchiParser#false.
    def enterFalse(self, ctx:BuchiParser.FalseContext):
        pass

    # Exit a parse tree produced by BuchiParser#false.
    def exitFalse(self, ctx:BuchiParser.FalseContext):
        pass


