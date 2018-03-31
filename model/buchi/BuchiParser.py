# Generated from Buchi.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from src.model.buchi.State import State
from src.model.buchi.Transition import Transition
from src.model.ltl.LTL import LTL

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\27")
        buf.write("k\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2\3\2\3\2\7\2\32\n\2\f")
        buf.write("\2\16\2\35\13\2\3\2\5\2 \n\2\3\2\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\6\3.\n\3\r\3\16\3/\3\3\3\3\3\3")
        buf.write("\5\3\65\n\3\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\5\6R\n\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\7\6^\n\6\f\6\16\6a\13\6\3\7\3\7\3\b\3\b\3\t\3")
        buf.write("\t\3\n\3\n\3\n\2\3\n\13\2\4\6\b\n\f\16\20\22\2\2\2l\2")
        buf.write("\24\3\2\2\2\4%\3\2\2\2\68\3\2\2\2\b:\3\2\2\2\nQ\3\2\2")
        buf.write("\2\fb\3\2\2\2\16d\3\2\2\2\20f\3\2\2\2\22h\3\2\2\2\24\25")
        buf.write("\7\3\2\2\25\37\7\4\2\2\26\27\5\4\3\2\27\30\b\2\1\2\30")
        buf.write("\32\3\2\2\2\31\26\3\2\2\2\32\35\3\2\2\2\33\31\3\2\2\2")
        buf.write("\33\34\3\2\2\2\34 \3\2\2\2\35\33\3\2\2\2\36 \5\f\7\2\37")
        buf.write("\33\3\2\2\2\37\36\3\2\2\2 !\3\2\2\2!\"\7\5\2\2\"#\3\2")
        buf.write("\2\2#$\7\2\2\3$\3\3\2\2\2%&\5\6\4\2&\64\7\6\2\2\'\65\7")
        buf.write("\7\2\2(\65\5\f\7\2)-\7\b\2\2*+\5\b\5\2+,\b\3\1\2,.\3\2")
        buf.write("\2\2-*\3\2\2\2./\3\2\2\2/-\3\2\2\2/\60\3\2\2\2\60\61\3")
        buf.write("\2\2\2\61\62\7\t\2\2\62\63\7\n\2\2\63\65\3\2\2\2\64\'")
        buf.write("\3\2\2\2\64(\3\2\2\2\64)\3\2\2\2\65\66\3\2\2\2\66\67\b")
        buf.write("\3\1\2\67\5\3\2\2\289\7\26\2\29\7\3\2\2\2:;\7\13\2\2;")
        buf.write("<\5\n\6\2<=\7\f\2\2=>\7\r\2\2>?\5\6\4\2?@\b\5\1\2@\t\3")
        buf.write("\2\2\2AR\b\6\1\2BC\7\16\2\2CD\5\n\6\2DE\7\17\2\2EF\b\6")
        buf.write("\1\2FR\3\2\2\2GH\5\20\t\2HI\b\6\1\2IR\3\2\2\2JK\7\20\2")
        buf.write("\2KL\5\n\6\6LM\b\6\1\2MR\3\2\2\2NO\5\16\b\2OP\b\6\1\2")
        buf.write("PR\3\2\2\2QA\3\2\2\2QB\3\2\2\2QG\3\2\2\2QJ\3\2\2\2QN\3")
        buf.write("\2\2\2R_\3\2\2\2ST\f\5\2\2TU\7\21\2\2UV\5\n\6\6VW\b\6")
        buf.write("\1\2W^\3\2\2\2XY\f\4\2\2YZ\7\22\2\2Z[\5\n\6\5[\\\b\6\1")
        buf.write("\2\\^\3\2\2\2]S\3\2\2\2]X\3\2\2\2^a\3\2\2\2_]\3\2\2\2")
        buf.write("_`\3\2\2\2`\13\3\2\2\2a_\3\2\2\2bc\5\22\n\2c\r\3\2\2\2")
        buf.write("de\7\27\2\2e\17\3\2\2\2fg\7\26\2\2g\21\3\2\2\2hi\7\23")
        buf.write("\2\2i\23\3\2\2\2\t\33\37/\64Q]_")
        return buf.getvalue()


class BuchiParser ( Parser ):

    grammarFileName = "Buchi.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'never'", "'{'", "'}'", "':'", "'skip'", 
                     "'if'", "'fi'", "';'", "'::'", "'->'", "'goto'", "'('", 
                     "')'", "'!'", "'&&'", "'||'", "'false;'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'1'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "WS", "BlockComment", "StringLiteral", 
                      "Unit" ]

    RULE_compilationUnit = 0
    RULE_stateDefinition = 1
    RULE_stateName = 2
    RULE_transition = 3
    RULE_expression = 4
    RULE_empty = 5
    RULE_unit = 6
    RULE_literal = 7
    RULE_false = 8

    ruleNames =  [ "compilationUnit", "stateDefinition", "stateName", "transition", 
                   "expression", "empty", "unit", "literal", "false" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    WS=18
    BlockComment=19
    StringLiteral=20
    Unit=21

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class CompilationUnitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.states_list = None
            self._stateDefinition = None # StateDefinitionContext

        def EOF(self):
            return self.getToken(BuchiParser.EOF, 0)

        def empty(self):
            return self.getTypedRuleContext(BuchiParser.EmptyContext,0)


        def stateDefinition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BuchiParser.StateDefinitionContext)
            else:
                return self.getTypedRuleContext(BuchiParser.StateDefinitionContext,i)


        def getRuleIndex(self):
            return BuchiParser.RULE_compilationUnit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompilationUnit" ):
                listener.enterCompilationUnit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompilationUnit" ):
                listener.exitCompilationUnit(self)




    def compilationUnit(self):

        localctx = BuchiParser.CompilationUnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_compilationUnit)
        localctx.states_list = []
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.match(BuchiParser.T__0)
            self.state = 19
            self.match(BuchiParser.T__1)

            self.state = 29
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BuchiParser.T__2, BuchiParser.StringLiteral]:
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BuchiParser.StringLiteral:
                    self.state = 20
                    localctx._stateDefinition = self.stateDefinition()
                    localctx.states_list.append(localctx._stateDefinition.s);
                    self.state = 27
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [BuchiParser.T__16]:
                self.state = 28
                self.empty()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 31
            self.match(BuchiParser.T__2)
            self.state = 33
            self.match(BuchiParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StateDefinitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.s = None
            self._stateName = None # StateNameContext
            self._transition = None # TransitionContext

        def stateName(self):
            return self.getTypedRuleContext(BuchiParser.StateNameContext,0)


        def empty(self):
            return self.getTypedRuleContext(BuchiParser.EmptyContext,0)


        def transition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BuchiParser.TransitionContext)
            else:
                return self.getTypedRuleContext(BuchiParser.TransitionContext,i)


        def getRuleIndex(self):
            return BuchiParser.RULE_stateDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStateDefinition" ):
                listener.enterStateDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStateDefinition" ):
                listener.exitStateDefinition(self)




    def stateDefinition(self):

        localctx = BuchiParser.StateDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stateDefinition)
        transitions_list = []
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            localctx._stateName = self.stateName()
            self.state = 36
            self.match(BuchiParser.T__3)
            self.state = 50
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BuchiParser.T__4]:
                self.state = 37
                self.match(BuchiParser.T__4)
                pass
            elif token in [BuchiParser.T__16]:
                self.state = 38
                self.empty()
                pass
            elif token in [BuchiParser.T__5]:
                self.state = 39
                self.match(BuchiParser.T__5)
                self.state = 43 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 40
                    localctx._transition = self.transition()
                    transitions_list.append(localctx._transition.t);
                    self.state = 45 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==BuchiParser.T__8):
                        break

                self.state = 47
                self.match(BuchiParser.T__6)
                self.state = 48
                self.match(BuchiParser.T__7)
                pass
            else:
                raise NoViableAltException(self)

            name_str = (None if localctx._stateName is None else self._input.getText((localctx._stateName.start,localctx._stateName.stop)));localctx.s =  State(name_str, transitions_list)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StateNameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def StringLiteral(self):
            return self.getToken(BuchiParser.StringLiteral, 0)

        def getRuleIndex(self):
            return BuchiParser.RULE_stateName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStateName" ):
                listener.enterStateName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStateName" ):
                listener.exitStateName(self)




    def stateName(self):

        localctx = BuchiParser.StateNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stateName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(BuchiParser.StringLiteral)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TransitionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.t = None
            self._expression = None # ExpressionContext
            self._stateName = None # StateNameContext

        def expression(self):
            return self.getTypedRuleContext(BuchiParser.ExpressionContext,0)


        def stateName(self):
            return self.getTypedRuleContext(BuchiParser.StateNameContext,0)


        def getRuleIndex(self):
            return BuchiParser.RULE_transition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTransition" ):
                listener.enterTransition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTransition" ):
                listener.exitTransition(self)




    def transition(self):

        localctx = BuchiParser.TransitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_transition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(BuchiParser.T__8)
            self.state = 57
            localctx._expression = self.expression(0)
            self.state = 58
            self.match(BuchiParser.T__9)
            self.state = 59
            self.match(BuchiParser.T__10)
            self.state = 60
            localctx._stateName = self.stateName()
            localctx.t =  Transition(localctx._expression.f, (None if localctx._stateName is None else self._input.getText((localctx._stateName.start,localctx._stateName.stop))))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.f = None
            self.left = None # ExpressionContext
            self._expression = None # ExpressionContext
            self._literal = None # LiteralContext
            self.unaryOperator = None # Token
            self.binaryOperator = None # Token
            self.right = None # ExpressionContext

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BuchiParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(BuchiParser.ExpressionContext,i)


        def literal(self):
            return self.getTypedRuleContext(BuchiParser.LiteralContext,0)


        def unit(self):
            return self.getTypedRuleContext(BuchiParser.UnitContext,0)


        def getRuleIndex(self):
            return BuchiParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BuchiParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                pass

            elif la_ == 2:
                self.state = 64
                self.match(BuchiParser.T__11)
                self.state = 65
                localctx._expression = self.expression(0)
                self.state = 66
                self.match(BuchiParser.T__12)
                localctx.f =  localctx._expression.f
                pass

            elif la_ == 3:
                self.state = 69
                localctx._literal = self.literal()
                localctx.f =  LTL.var((None if localctx._literal is None else self._input.getText((localctx._literal.start,localctx._literal.stop))))
                pass

            elif la_ == 4:
                self.state = 72
                localctx.unaryOperator = self.match(BuchiParser.T__13)
                self.state = 73
                localctx._expression = self.expression(4)
                localctx.f =  LTL.not_(localctx._expression.f)
                pass

            elif la_ == 5:
                self.state = 76
                self.unit()
                localctx.f =  LTL.t()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 93
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 91
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = BuchiParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 81
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 82
                        localctx.binaryOperator = self.match(BuchiParser.T__14)
                        self.state = 83
                        localctx.right = localctx._expression = self.expression(4)
                        localctx.f =  LTL.and_(localctx.left.f, localctx.right.f)
                        pass

                    elif la_ == 2:
                        localctx = BuchiParser.ExpressionContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 86
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 87
                        localctx.binaryOperator = self.match(BuchiParser.T__15)
                        self.state = 88
                        localctx.right = localctx._expression = self.expression(3)
                        localctx.f =  LTL.or_(localctx.left.f, localctx.right.f)
                        pass

             
                self.state = 95
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class EmptyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def false(self):
            return self.getTypedRuleContext(BuchiParser.FalseContext,0)


        def getRuleIndex(self):
            return BuchiParser.RULE_empty

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmpty" ):
                listener.enterEmpty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmpty" ):
                listener.exitEmpty(self)




    def empty(self):

        localctx = BuchiParser.EmptyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_empty)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.false()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class UnitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Unit(self):
            return self.getToken(BuchiParser.Unit, 0)

        def getRuleIndex(self):
            return BuchiParser.RULE_unit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnit" ):
                listener.enterUnit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnit" ):
                listener.exitUnit(self)




    def unit(self):

        localctx = BuchiParser.UnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_unit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(BuchiParser.Unit)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def StringLiteral(self):
            return self.getToken(BuchiParser.StringLiteral, 0)

        def getRuleIndex(self):
            return BuchiParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = BuchiParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(BuchiParser.StringLiteral)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FalseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BuchiParser.RULE_false

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFalse" ):
                listener.enterFalse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFalse" ):
                listener.exitFalse(self)




    def false(self):

        localctx = BuchiParser.FalseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_false)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(BuchiParser.T__16)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




