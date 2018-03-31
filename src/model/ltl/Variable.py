from src.model.ltl import LTLVisitor
from src.model.ltl.Formula import Formula
from src.model.ltl.Not import Not


class Variable(Formula):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return str(self.name)

    def toNormalForm(self, negation: bool) -> Formula:
        return Not(self) if negation else self

    def map_(self, mapper) -> Formula:
        return Variable(mapper(self.name))

    def accept(self, visitor: LTLVisitor):
        visitor.visit_Variable(self)

    def negation(self) -> Formula:
        return self
