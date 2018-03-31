from src.model.ltl import LTLVisitor
from src.model.ltl.Formula import Formula


class Next(Formula):
    def __init__(self, f: Formula):
        self.f = f

    def __str__(self):
        return "(X " + str(self.f) + ")"

    def toNormalForm(self, negation: bool) -> Formula:
        return Next(self.f.toNormalForm(negation))

    def map_(self, mapper) -> Formula:
        return Next(self.f.map_(mapper))

    def accept(self, visitor: LTLVisitor):
        visitor.visit_Next(self)

    def negation(self) -> Formula:
        return self
