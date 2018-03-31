from src.model.ltl.BinaryFormula import BinaryFormula
from src.model.ltl.BinaryOperation import AND, OR
from src.model.ltl.Const import Const
from src.model.ltl.LTL import LTL

from src.model.ltl.LTLVisitor import LTLVisitor
from src.model.ltl.Next import Next
from src.model.ltl.Not import Not
from src.model.ltl.Variable import Variable


class LTLIntersector(object):
    def intersect(self, a, b):
        variables = set()
        if a != LTL.t():
            visitor = VariableVisitor()
            a.accept(visitor)
            variables = visitor.getResult()

        markVisitor = MarkVisitor(variables)
        b.accept(markVisitor)
        return a if markVisitor.getMark() else None


class MarkVisitor(LTLVisitor):
    def __init__(self, trueVariables):
        self.trues = trueVariables
        self.mark = False

    def getMark(self):
        return self.mark

    def visit_BinaryFormula(self, binary: BinaryFormula) -> None:
        binary.left.accept(self)
        left = self.mark
        binary.right.accept(self)
        right = self.mark
        if binary.operation == OR():
            self.mark = left or right
            return

        if binary.operation == AND():
            self.mark = left and right
            return

        raise Exception()

    def visit_Const(self, c: Const) -> None:
        self.mark = c.isTrue

    def visit_Not(self, formula: Not) -> None:
        formula.f.accept(self)
        self.mark = not self.mark

    def visit_Next(self, formula: Next) -> None:
        raise Exception()

    def visit_Variable(self, variable: Variable) -> None:
        self.mark = variable in self.trues


class VariableVisitor(LTLVisitor):
    def __init__(self):
        self.variables = set()

    def getResult(self) -> set:
        return self.variables

    def visit_BinaryFormula(self, binary: BinaryFormula) -> None:
        if binary.operation != AND():
            raise Exception()
        binary.left.accept(self)
        binary.right.accept(self)

    def visit_Const(self, c: Const) -> None:
        raise Exception()

    def visit_Not(self, formula: Not) -> None:
        raise Exception()

    def visit_Next(self, formula: Next) -> None:
        raise Exception()

    def visit_Variable(self, variable: Variable) -> None:
        self.variables.add(variable)
