# Generated from LTL.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from src.model.ltl.LTL import LTL

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\23")
        buf.write("T\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2\31\n\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\7\29\n\2\f\2\16\2<\13\2\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\5\3J\n\3\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\5\4R\n\4\3\4\2\3\2\5\2\4\6\2\2\2^\2\30\3\2\2\2\4")
        buf.write("I\3\2\2\2\6Q\3\2\2\2\b\31\b\2\1\2\t\n\5\4\3\2\n\13\b\2")
        buf.write("\1\2\13\31\3\2\2\2\f\r\7\n\2\2\r\16\5\2\2\13\16\17\b\2")
        buf.write("\1\2\17\31\3\2\2\2\20\21\7\13\2\2\21\22\5\2\2\n\22\23")
        buf.write("\b\2\1\2\23\31\3\2\2\2\24\25\7\f\2\2\25\26\5\2\2\t\26")
        buf.write("\27\b\2\1\2\27\31\3\2\2\2\30\b\3\2\2\2\30\t\3\2\2\2\30")
        buf.write("\f\3\2\2\2\30\20\3\2\2\2\30\24\3\2\2\2\31:\3\2\2\2\32")
        buf.write("\33\f\b\2\2\33\34\7\t\2\2\34\35\5\2\2\t\35\36\b\2\1\2")
        buf.write("\369\3\2\2\2\37 \f\7\2\2 !\7\b\2\2!\"\5\2\2\b\"#\b\2\1")
        buf.write("\2#9\3\2\2\2$%\f\6\2\2%&\7\4\2\2&\'\5\2\2\7\'(\b\2\1\2")
        buf.write("(9\3\2\2\2)*\f\5\2\2*+\7\3\2\2+,\5\2\2\6,-\b\2\1\2-9\3")
        buf.write("\2\2\2./\f\4\2\2/\60\7\6\2\2\60\61\5\2\2\4\61\62\b\2\1")
        buf.write("\2\629\3\2\2\2\63\64\f\3\2\2\64\65\7\7\2\2\65\66\5\2\2")
        buf.write("\4\66\67\b\2\1\2\679\3\2\2\28\32\3\2\2\28\37\3\2\2\28")
        buf.write("$\3\2\2\28)\3\2\2\28.\3\2\2\28\63\3\2\2\29<\3\2\2\2:8")
        buf.write("\3\2\2\2:;\3\2\2\2;\3\3\2\2\2<:\3\2\2\2=>\5\6\4\2>?\b")
        buf.write("\3\1\2?J\3\2\2\2@A\7\17\2\2AB\5\2\2\2BC\7\20\2\2CD\b\3")
        buf.write("\1\2DJ\3\2\2\2EF\7\5\2\2FG\5\2\2\2GH\b\3\1\2HJ\3\2\2\2")
        buf.write("I=\3\2\2\2I@\3\2\2\2IE\3\2\2\2J\5\3\2\2\2KL\7\r\2\2LR")
        buf.write("\b\4\1\2MN\7\16\2\2NR\b\4\1\2OP\7\21\2\2PR\b\4\1\2QK\3")
        buf.write("\2\2\2QM\3\2\2\2QO\3\2\2\2R\7\3\2\2\2\7\308:IQ")
        return buf.getvalue()


class LTLParser ( Parser ):

    grammarFileName = "LTL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'|'", "'&'", "'!'", "'->'", "'<->'", 
                     "'U'", "'R'", "'X'", "'G'", "'F'", "'true'", "'false'", 
                     "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "DIS", "CON", "NOT", "IMPL", "EQ", "UNTIL", 
                      "RELEASE", "NEXT", "GLOB", "FUTURE", "TRUE", "FALSE", 
                      "LP", "RP", "StringLiteral", "WS", "ErrorChar" ]

    RULE_ltl = 0
    RULE_primary = 1
    RULE_constant = 2

    ruleNames =  [ "ltl", "primary", "constant" ]

    EOF = Token.EOF
    DIS=1
    CON=2
    NOT=3
    IMPL=4
    EQ=5
    UNTIL=6
    RELEASE=7
    NEXT=8
    GLOB=9
    FUTURE=10
    TRUE=11
    FALSE=12
    LP=13
    RP=14
    StringLiteral=15
    WS=16
    ErrorChar=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class LtlContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.f = None
            self.l = None # LtlContext
            self._primary = None # PrimaryContext
            self._ltl = None # LtlContext
            self.r = None # LtlContext

        def primary(self):
            return self.getTypedRuleContext(LTLParser.PrimaryContext,0)


        def NEXT(self):
            return self.getToken(LTLParser.NEXT, 0)

        def ltl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LTLParser.LtlContext)
            else:
                return self.getTypedRuleContext(LTLParser.LtlContext,i)


        def GLOB(self):
            return self.getToken(LTLParser.GLOB, 0)

        def FUTURE(self):
            return self.getToken(LTLParser.FUTURE, 0)

        def RELEASE(self):
            return self.getToken(LTLParser.RELEASE, 0)

        def UNTIL(self):
            return self.getToken(LTLParser.UNTIL, 0)

        def CON(self):
            return self.getToken(LTLParser.CON, 0)

        def DIS(self):
            return self.getToken(LTLParser.DIS, 0)

        def IMPL(self):
            return self.getToken(LTLParser.IMPL, 0)

        def EQ(self):
            return self.getToken(LTLParser.EQ, 0)

        def getRuleIndex(self):
            return LTLParser.RULE_ltl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLtl" ):
                listener.enterLtl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLtl" ):
                listener.exitLtl(self)



    def ltl(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LTLParser.LtlContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 0
        self.enterRecursionRule(localctx, 0, self.RULE_ltl, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                pass

            elif la_ == 2:
                self.state = 7
                localctx._primary = self.primary()
                localctx.f =  localctx._primary.f
                pass

            elif la_ == 3:
                self.state = 10
                self.match(LTLParser.NEXT)
                self.state = 11
                localctx._ltl = self.ltl(9)
                localctx.f =  LTL.next_(localctx._ltl.f)
                pass

            elif la_ == 4:
                self.state = 14
                self.match(LTLParser.GLOB)
                self.state = 15
                localctx._ltl = self.ltl(8)
                localctx.f =  LTL.globally(localctx._ltl.f)
                pass

            elif la_ == 5:
                self.state = 18
                self.match(LTLParser.FUTURE)
                self.state = 19
                localctx._ltl = self.ltl(7)
                localctx.f =  LTL.future(localctx._ltl.f)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 56
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 54
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = LTLParser.LtlContext(self, _parentctx, _parentState)
                        localctx.l = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ltl)
                        self.state = 24
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 25
                        self.match(LTLParser.RELEASE)
                        self.state = 26
                        localctx.r = localctx._ltl = self.ltl(7)
                        localctx.f =  LTL.release(localctx.l.f, localctx.r.f)
                        pass

                    elif la_ == 2:
                        localctx = LTLParser.LtlContext(self, _parentctx, _parentState)
                        localctx.l = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ltl)
                        self.state = 29
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 30
                        self.match(LTLParser.UNTIL)
                        self.state = 31
                        localctx.r = localctx._ltl = self.ltl(6)
                        localctx.f =  LTL.until(localctx.l.f, localctx.r.f)
                        pass

                    elif la_ == 3:
                        localctx = LTLParser.LtlContext(self, _parentctx, _parentState)
                        localctx.l = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ltl)
                        self.state = 34
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 35
                        self.match(LTLParser.CON)
                        self.state = 36
                        localctx.r = localctx._ltl = self.ltl(5)
                        localctx.f =  LTL.and_(localctx.l.f, localctx.r.f)
                        pass

                    elif la_ == 4:
                        localctx = LTLParser.LtlContext(self, _parentctx, _parentState)
                        localctx.l = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ltl)
                        self.state = 39
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 40
                        self.match(LTLParser.DIS)
                        self.state = 41
                        localctx.r = localctx._ltl = self.ltl(4)
                        localctx.f =  LTL.or_(localctx.l.f, localctx.r.f)
                        pass

                    elif la_ == 5:
                        localctx = LTLParser.LtlContext(self, _parentctx, _parentState)
                        localctx.l = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ltl)
                        self.state = 44
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 45
                        self.match(LTLParser.IMPL)
                        self.state = 46
                        localctx.r = localctx._ltl = self.ltl(2)
                        localctx.f =  LTL.impl(localctx.l.f, localctx.r.f)
                        pass

                    elif la_ == 6:
                        localctx = LTLParser.LtlContext(self, _parentctx, _parentState)
                        localctx.l = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_ltl)
                        self.state = 49
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 50
                        self.match(LTLParser.EQ)
                        self.state = 51
                        localctx.r = localctx._ltl = self.ltl(2)
                        localctx.f =  LTL.eq(localctx.l.f, localctx.r.f)
                        pass

             
                self.state = 58
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class PrimaryContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.f = None
            self._constant = None # ConstantContext
            self._ltl = None # LtlContext

        def constant(self):
            return self.getTypedRuleContext(LTLParser.ConstantContext,0)


        def LP(self):
            return self.getToken(LTLParser.LP, 0)

        def ltl(self):
            return self.getTypedRuleContext(LTLParser.LtlContext,0)


        def RP(self):
            return self.getToken(LTLParser.RP, 0)

        def NOT(self):
            return self.getToken(LTLParser.NOT, 0)

        def getRuleIndex(self):
            return LTLParser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)




    def primary(self):

        localctx = LTLParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_primary)
        try:
            self.state = 71
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LTLParser.TRUE, LTLParser.FALSE, LTLParser.StringLiteral]:
                self.enterOuterAlt(localctx, 1)
                self.state = 59
                localctx._constant = self.constant()
                localctx.f =  localctx._constant.f
                pass
            elif token in [LTLParser.LP]:
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                self.match(LTLParser.LP)
                self.state = 63
                localctx._ltl = self.ltl(0)
                self.state = 64
                self.match(LTLParser.RP)
                localctx.f =  localctx._ltl.f
                pass
            elif token in [LTLParser.NOT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 67
                self.match(LTLParser.NOT)
                self.state = 68
                localctx._ltl = self.ltl(0)
                localctx.f =  LTL.not_(localctx._ltl.f)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConstantContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.f = None
            self._StringLiteral = None # Token

        def TRUE(self):
            return self.getToken(LTLParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(LTLParser.FALSE, 0)

        def StringLiteral(self):
            return self.getToken(LTLParser.StringLiteral, 0)

        def getRuleIndex(self):
            return LTLParser.RULE_constant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstant" ):
                listener.enterConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstant" ):
                listener.exitConstant(self)




    def constant(self):

        localctx = LTLParser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_constant)
        try:
            self.state = 79
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LTLParser.TRUE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 73
                self.match(LTLParser.TRUE)
                localctx.f =  LTL.t()
                pass
            elif token in [LTLParser.FALSE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                self.match(LTLParser.FALSE)
                localctx.f =  LTL.f()
                pass
            elif token in [LTLParser.StringLiteral]:
                self.enterOuterAlt(localctx, 3)
                self.state = 77
                localctx._StringLiteral = self.match(LTLParser.StringLiteral)
                name = (None if localctx._StringLiteral is None else localctx._StringLiteral.text);localctx.f =  LTL.var(name[1:-1])
                pass
            else:
                raise NoViableAltException(self)

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
        self._predicates[0] = self.ltl_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def ltl_sempred(self, localctx:LtlContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 1)
         




