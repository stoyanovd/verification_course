from src.model.ltl.BinaryFormula import BinaryFormula
from src.model.ltl.BinaryOperation import AND, OR, R, U
from src.model.ltl.Const import Const
from src.model.ltl.Formula import Formula
from src.model.ltl.Next import Next
from src.model.ltl.Not import Not
from src.model.ltl.Variable import Variable


class LTL:
    @staticmethod
    def and_(l: Formula, r: Formula) -> Formula:
        return BinaryFormula(AND(), l, r)

    @staticmethod
    def or_(l: Formula, r: Formula) -> Formula:
        return BinaryFormula(OR(), l, r)

    @staticmethod
    def release(l: Formula, r: Formula) -> Formula:
        return BinaryFormula(R(), l, r)

    @staticmethod
    def until(l: Formula, r: Formula) -> Formula:
        return BinaryFormula(U(), l, r)

    @staticmethod
    def eq(l: Formula, r: Formula) -> Formula:
        return BinaryFormula(AND(), LTL.impl(l, r), LTL.impl(r, l))

    @staticmethod
    def impl(l: Formula, r: Formula) -> Formula:
        return BinaryFormula(OR(), Not(l), r)

    @staticmethod
    def not_(f: Formula) -> Formula:
        return Not(f)

    @staticmethod
    def next_(f: Formula) -> Formula:
        return Next(f)

    @staticmethod
    def var(var) -> Formula:
        return Variable(var)

    @staticmethod
    def future(f: Formula) -> Formula:
        return BinaryFormula(U(), LTL.t(), f)

    @staticmethod
    def t() -> Formula:
        return Const(True)

    @staticmethod
    def globally(f: Formula) -> Formula:
        return BinaryFormula(R(), LTL.f(), f)

    @staticmethod
    def f() -> Formula:
        return Const(False)
