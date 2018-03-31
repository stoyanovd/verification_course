from src.model.ltl import LTLVisitor
from src.model.ltl.Formula import Formula


class Const(Formula):
    def __init__(self, isTrue: bool):
        self.isTrue = isTrue

    def toNormalForm(self, negation: bool) -> Formula:
        return Const(not self.isTrue) if negation else self

    def map_(self, mapper) -> Formula:
        return Const(self.isTrue)

    def accept(self, visitor: LTLVisitor) -> None:
        visitor.visit_Const(self)

    def negation(self) -> Formula:
        return Const(not self.isTrue)

    def __str__(self):
        return "true" if self.isTrue else "false"
