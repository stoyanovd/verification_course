from src.model.ltl import LTLVisitor
from src.model.ltl.Formula import Formula


class Not(Formula):
    f: Formula

    def __init__(self, f: Formula):
        self.f = f

    def __str__(self):
        return "!" + str(self.f)

    def toNormalForm(self, negation: bool) -> Formula:
        return self.f.toNormalForm(not negation)

    def map_(self, mapper) -> Formula:
        return Not(self.f.map_(mapper))

    def accept(self, visitor: LTLVisitor) -> None:
        visitor.visit_Not(self)

    def negation(self) -> Formula:
        return self.f
